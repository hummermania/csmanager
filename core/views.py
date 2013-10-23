from django.http import Http404
from django.shortcuts import redirect, get_object_or_404
from django.forms import ModelForm

from annoying.decorators import render_to

from core.models import Client, Server

class ClientForm(ModelForm):
    class Meta:
        model = Client

class ServerForm(ModelForm):
    class Meta:
        model = Server

@render_to('home.html')
def home_page(request):
    page_title = 'Django app.'
    return {'page_title': page_title}


@render_to('clients.html')
def client_index(request):
    clients = Client.objects.all().order_by('server_id')
    return {'clients': clients}


@render_to('clients.html')
def client_details(request, client_id):
    if request.method == 'POST':
        client = Client.objects.get(pk=client_id)
        client_form = ClientForm(request.POST, instance = client)

        if client.server_id != request.POST.get('server_id'):
            if request.POST.get('active', None) == None:
                error = "Inactive client can't move to another server"
                return {'error': error, 'form' : client_form}
        
        if client_form.is_valid():
            client_form.save()
        return {'form' : client_form} #redirect('client_index')

    else:
        client = get_object_or_404(Client, pk = client_id)
        form = ClientForm(instance = client)
        return {'form' : form } 



@render_to('servers.html')
def server_index(request):
    servers = Server.objects.all().order_by('name')
    return {'servers': servers}


@render_to('servers.html')
def server_details(request, server_id):
    if request.method == 'POST':
        server = Server.objects.get(pk=server_id)
        server_form = ServerForm(request.POST, instance = server)

        if server_form.is_valid():
            server_form.save()
        return {'form' : server_form} #redirect('client_index')

    else:
        server = get_object_or_404(Server, pk = server_id)

        form = ServerForm(instance = server)

        client_list = Client.objects.filter(server_id = server.pk).order_by('name')
        return {'form': form, 'client_list' : client_list } 
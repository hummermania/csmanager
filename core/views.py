import logging

from django.http import Http404
from django.shortcuts import redirect, get_object_or_404
from django.forms import ModelForm, BooleanField, RadioSelect
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS

from annoying.decorators import render_to

from core.models import Client

logger = logging.getLogger(__name__)

class ClientForm(ModelForm):
    class Meta:
        model = Client

@render_to('home.html')
def home_page(request):
    page_title = 'Django app.'
    return {'page_title': page_title}


@render_to('clients.html')
def client_index(request):
    clients = Client.objects.all()
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
            logger.info("Save client!")
        return {'form' : client_form} #redirect('client_index')

    else:
        client = get_object_or_404(Client, pk = client_id)
        form = ClientForm(instance = client)
        return {'form' : form } 


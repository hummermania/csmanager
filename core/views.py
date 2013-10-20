# Create your views here.
from django.http import Http404
from django.shortcuts import redirect, get_object_or_404
from django.forms import ModelForm

from annoying.decorators import render_to

from core.models import Client


class ClientForm(ModelForm):
	class Meta:
		model = Client
		#fields = ("pk","server_id","name","active")

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
	# TODO: Find why boolean field "active" not save in request
	if request.method == 'POST':
		form = ClientForm(request.POST)
		if form.is_valid():
			new_client = form.save(commit = False)
			new_client.id = client_id
			new_client.save()
		return redirect('client_index')

	else:
		client = get_object_or_404(Client, pk = client_id)
		form = ClientForm(instance = client)
		return {'form' : form }	


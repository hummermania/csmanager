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
	# TODO: Saving data in progress...
	if request.method == 'POST':
		client = get_object_or_404(Client, pk = client_id)#request.POST.get('client_id'))
		form = ClientForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('client_index')

	else:
		# TODO: On this code rendering form haven't PK of model, 
		# and every save - create new object in database
		client = get_object_or_404(Client, pk = client_id)
		form = ClientForm(instance = client)
		return {'form' : form }	


# Create your views here.

from annoying.decorators import render_to


@render_to('home.html')
def home_page(request):
	page_title = 'Django app.'
	return {'page_title': page_title}# Create your views here.

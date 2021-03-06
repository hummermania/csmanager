from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'core.views.home_page', name='home'),
    
    url(r'^clients/$', 'core.views.client_index', name='client_index'),
    url(r'^client/(\d+)/$', 'core.views.client_details', name='client_details'),

    url(r'^servers/$', 'core.views.server_index', name='server_index'),
    url(r'^server/(\d+)/$', 'core.views.server_details', name='server_details'),

    # url(r'^csmanager/', include('csmanager.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

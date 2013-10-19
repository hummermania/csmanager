from django.contrib import admin
from core.models import Server, Client


class ServersAdmin(admin.ModelAdmin):
	pass

class ClientsAdmin(admin.ModelAdmin):
	pass

admin.site.register(Server, ServersAdmin)
admin.site.register(Client, ClientsAdmin)

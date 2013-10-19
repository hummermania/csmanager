from django.db import models
from django.contrib import admin

# Create your models here.
class Server(models.Model):
    name = models.CharField(max_length = 100, blank = False)
    ip = models.CharField(max_length = 15)

    def __str__(self):
        return self.name + ", ipv4 = " + self.ip

# Create your models here.
class Client(models.Model):
    server_id = models.ForeignKey(Server)
    name = models.CharField(max_length=100, blank = False)
    active = models.BooleanField(default = True)
    
    def __str__(self):
        return self.name
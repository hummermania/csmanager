from django.db import models
from django.contrib import admin

# Create your models here.
class Servers(models.Model):
    name = models.CharField(max_length = 100, blank = False)
    ip = models.CharField(max_length = 15)

    def __str__(self):
        return self.name

# Create your models here.
class Clients(models.Model):
    server_id = models.ForeignKey(Servers)
    name = models.CharField(max_length=100, blank = False)
    active = models.BooleanField(default = False)

from django.db import models

# Create your models here.
class Servers(models.Model):
	name = models.CharField(max_length = 100, blank = False)
	ip = models.CharField(max_length = 15)

# Create your models here.
class Client(models.Model):
	server_id = models.ForeignKey(Servers)
	name = models.CharField(max_length=100, blank = False)
	active = models.BooleanField(default = False)


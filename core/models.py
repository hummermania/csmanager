import logging

from django.db import models
from django.contrib import admin



logger = logging.getLogger(__name__)

YES_NO = (
    ( 1 , 'Yes'),
    ( 0 , 'No'),
)


# Create your models here.
class Server(models.Model):
    name = models.CharField(max_length = 100, blank = False, unique= True)
    ip = models.GenericIPAddressField(protocol = 'both', unique= True)

    def __unicode__(self):
        return u'%s, ipv4 = %s' % (self.name, self.ip)


class Client(models.Model):
    server_id = models.ForeignKey(Server)
    name = models.CharField(max_length=100, blank = False)
    active = models.BooleanField(default = True)#choices = YES_NO)
    
    def __unicode__(self):
        return u'[%s],  Client = "%s", Active = "%s"' % (self.server_id.name, self.name, self.active)

    
    class Meta:
        unique_together = ("server_id", "name")

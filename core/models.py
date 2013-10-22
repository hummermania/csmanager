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
    name = models.CharField(max_length = 100, blank = False)
    ip = models.GenericIPAddressField(protocol = 'both')

    def __unicode__(self):
        return u'%s, %s, ipv4 = %s' % (self.pk, self.name, self.ip)


class Client(models.Model):
    server_id = models.ForeignKey(Server)
    name = models.CharField(max_length=100, blank = False)
    active = models.BooleanField()#choices = YES_NO)
    
    def __unicode__(self):
        return u'[%s],  Client = "%s"' % (self.server_id.name, self.name)

    
    class Meta:
        unique_together = ("server_id", "name")

from django.db import models
from django.contrib import admin

class Server(models.Model):
    name = models.CharField(max_length = 100, blank = False)
    ip = models.GenericIPAddressField(protocol = 'both', unique= True)

    def __unicode__(self):
        return u'%s, ipv4 = %s' % (self.name, self.ip)
    
    class Meta:
        unique_together = ("name", "ip")


class Client(models.Model):
    server_id = models.ForeignKey(Server)
    name = models.CharField(max_length=100, blank = False)
    active = models.BooleanField(default = True)#choices = YES_NO)
    
    def __unicode__(self):
        return u'[%s],  Client = "%s", Active = "%s"' % (self.server_id.name, self.name, self.active)

    
    class Meta:
        unique_together = ("server_id", "name")

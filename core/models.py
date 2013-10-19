from django.db import models
from django.contrib import admin
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS

# Create your models here.
class Server(models.Model):
    name = models.CharField(max_length = 100, blank = False)
    ip = models.CharField(max_length = 15)

    def __unicode__(self):
        return u'%s, ipv4 = %s' % (self.name, self.ip)


class Client(models.Model):
    server_id = models.ForeignKey(Server)
    name = models.CharField(max_length=100, blank = False)
    active = models.BooleanField(default = True)
    
    def __unicode__(self):
        return u'[%s],  Client = "%s"' % (self.server_id.name, self.name)


    def save(self, *args, **kwargs):
        if self.pk is not None:
            orig = self.__class__.objects.get(pk = self.pk)
            old_server = orig.server_id
            new_server = self.server_id
            if old_server != new_server: # only when the server change
                if self.active == False: # only new state is importand
                    raise ValidationError("Inactive client can't move to another server")

        super(Client, self).save(*args, **kwargs)
    
    class Meta:
        unique_together = ("server_id", "name")

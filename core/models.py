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
        #TODO: Add Server name before client name
        return self.name


    def validate_unique(self, exclude=None):
        super(Client, self).validate_unique()
        query_set = Client.objects.filter(name=self.name)
        if query_set.filter(server_id=self.server_id).exists():
            raise ValidationError(
                {
                    NON_FIELD_ERRORS:
                    ('Client name must be unique per Server!',)
                }
            )

    def save(self, *args, **kwargs):

        self.validate_unique()

        super(Client, self).save(*args, **kwargs)
    
    # If we use unique_together it override "validate_unique" on the low level
    # and don't allow to raise custom error message
    #class Meta:
        #unique_together = ("server_id", "name")
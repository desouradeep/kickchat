from django.db import models

class message(models.Model):
    def __unicode__(self):
        return self.message
    username = models.CharField(max_length=100)
    time = models.DateTimeField()
    message = models.CharField(max_length=1000)


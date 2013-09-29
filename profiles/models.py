from django.db import models
from django.contrib.auth.models import User

class CustomUser(models.Model):
    def __unicode__(self):
        return self.user.username
    user = models.ForeignKey(User)
    fb_profile = models.URLField(max_length=200, unique=True, null=True)
    is_online = models.BooleanField()

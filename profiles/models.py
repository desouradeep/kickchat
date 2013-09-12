from django.db import models
from django.contrib.auth.models import User

class CustomUser(models.Model):
    def __unicode__(self):
        return self.roll_no
    user = models.ForeignKey(User)
    roll_no = models.CharField(max_length=6, primary_key=True)
    fb_profile = models.URLField(max_length=200, unique=True)
    is_online = models.BooleanField()
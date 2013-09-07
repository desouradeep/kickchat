from django.db import models

class user(models.Model):
    def __unicode__(self):
        return self.username
    username = models.CharField(max_length=100, unique=True)
    roll_no = models.CharField(max_length=6, primary_key=True)
    fullname = models.CharField(max_length=200)
    fb_profile = models.URLField(max_length=200, unique=True)
    email_id = models.EmailField(max_length=100, unique=True)
    is_online = models.BooleanField()
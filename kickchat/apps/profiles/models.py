from django.db import models
from django.contrib.auth.models import User
from jsonfield import JSONField
from django.conf import settings
from os import path


def content_file_name(instance, filename):
    return path.join(settings.STATIC_URL, 'UserProfile',
                     instance.user.username, filename)


class UserProfile(models.Model):
    class Meta:
        verbose_name = 'UserProfile'
        verbose_name_plural = 'UserProfiles'

    def __unicode__(self):
        return self.user.username

    user = models.ForeignKey(User, null=False, unique=True)
    profile_picture = models.ImageField(null=True, upload_to=content_file_name)
    bio = models.TextField(null=True)
    birthday = models.DateField(null=True)
    education = JSONField(null=True)
    gender = models.CharField(max_length=20, null=True)
    hometown = models.CharField(max_length=100, null=True)
    interests = JSONField(null=True)
    languages = JSONField(null=True)
    facebook_username = models.CharField(max_length=200, null=True,
                                         unique=True)
    facebook_url = models.URLField(max_length=255, null=True, unique=True)
    location = models.CharField(max_length=100, null=True)
    relationship_status = models.CharField(max_length=100, null=True)
    website = models.URLField(max_length=400, null=True)
    work = JSONField(null=True)
    facebook_details = JSONField(null=True)


class Post(models.Model):
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __unicode__(self):
        return self.id + ' - ' + self.text[:10]

    id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(null=False, auto_now=True)
    user = models.ForeignKey(User, null=False)
    location = models.CharField(max_length=100, null=True)
    text = models.TextField(null=False)
    tags = JSONField(null=True)
    pictures = JSONField(null=True)
    link = models.URLField(max_length=200, null=True)

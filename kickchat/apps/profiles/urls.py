from django.conf.urls import patterns, url
from profiles import views

urlpatterns = patterns('',
        url(r'^$', views.index),
        url(r'^(?P<username>.+?)/$', views.index),
    )
from django.conf.urls import patterns, url
from chat import views

urlpatterns = patterns('',
        url(r'^$', views.index),
    )

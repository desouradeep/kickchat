from django.conf.urls import patterns, url
from profiles import views

urlpatterns = patterns('',
        url(r'^login', views.login),
        url(r'^logout', views.logout),
        url(r'^$', views.index),
    )

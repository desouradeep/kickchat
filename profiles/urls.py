from django.conf.urls import patterns, url
from profiles import views

urlpatterns = patterns('',
        url(r'^login/', views.login_user),
        url(r'^logout/', views.logout_user),
        url(r'^register/', views.register),
        url(r'^$', views.index),
    )

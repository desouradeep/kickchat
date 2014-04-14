from django.conf.urls import patterns, url
from home import views, pagelets

urlpatterns = patterns('',
    url(r'^$', views.index, name='home-index'),
    # Pagelets
    url(r'^feed/$', pagelets.feed, name='home-feed'),
    url(r'^signin/$', pagelets.signin, name='home-signin'),
    url(r'^register/$', pagelets.register, name='home-register'),
    )

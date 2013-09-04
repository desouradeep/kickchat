from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'offchat.views.home', name='home'),
    # url(r'^offchat/', include('offchat.foo.urls')),
    url(r'^chat/', include('chat.urls',namespace='chat')),
    url(r'^profile/', include('profiles.urls',namespace='profile')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

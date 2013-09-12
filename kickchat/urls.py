from django.conf.urls import patterns, include, url
from kickchat import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'offchat.views.home', name='home'),
    # url(r'^offchat/', include('offchat.foo.urls')),
    url(r'^chat/', include('chat.urls',namespace='chat')),
    url(r'^profile/', include('profiles.urls',namespace='profile')),
    url(r'^search/', include('search.urls',namespace='search')),
    url(r'^about/', views.about),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

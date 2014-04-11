from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'home.views.index', name='home'),
    url(r'^chat/', 'chat.views.index', name='chat'),
    url(r'^profile/', 'profiles.views.index', name='profile'),
    url(r'^search/', 'search.views.index', name='search'),
    url(r'^groups/', 'groups.views.index', name='groups'),
    url(r'^about/', 'home.views.about', name='about'),

    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',
     {'next_page': '/'}),
    url(r'^accounts/', include('allauth.urls')),

    # url(r'^kickchat/', include('kickchat.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

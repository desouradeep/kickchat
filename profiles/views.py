from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
activated_navbar_element = 'profile'
from profiles.models import CustomUser

def index(request, *args, **kwargs):
    if not request.user.is_authenticated():
        return redirect('/')

    current_user = User.objects.get(username=request.user.username)

    if len(kwargs) == 1:
        username = kwargs.pop('username')
        query_user = User.objects.get(username=username)
    else:
        query_user = current_user

    context = RequestContext(request, {
        'activated_navbar_element': activated_navbar_element,
        'query_user' : query_user,
        'request_user' : request.user,
        })
    return render_to_response('profile/profile.html', context_instance=context)

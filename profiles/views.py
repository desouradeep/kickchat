from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
activated_navbar_element = 'profile'

def login(request):
    return HttpResponse('Login page')

def logout(request):
    return HttpResponse('Logout page')

def index(request):
    context = RequestContext(request, {
        'activated_navbar_element': activated_navbar_element,
        })
    return render_to_response('profile.html', context_instance=context)


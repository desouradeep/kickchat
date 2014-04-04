# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, render_to_response, redirect
from django.template import Context, RequestContext

def index(request):
    context = RequestContext(request, {
            'activate_navbar_element' : 'kickchat'
    })
    return render_to_response('home/home.html', context_instance=context)

def about(request):
    context = RequestContext(request, {
            'activate_navbar_element_id' : 'about'
    })
    return render_to_response('home/about.html', context_instance=context)

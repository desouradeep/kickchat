# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, render_to_response, redirect
from django.template import Context, RequestContext

def index(request):
    context = RequestContext(request, {
            'text' : 'hello world'
        })
    return render_to_response('base/base.html', context_instance=context)

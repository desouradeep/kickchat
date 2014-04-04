# Create your views here.
from django.shortcuts import render, render_to_response, redirect
from django.template import Context, RequestContext

def index(request):
    context = RequestContext(request, {
            'activate_navbar_element_id' : 'chat'
        })
    return render_to_response('chat/chat.html', context_instance=context)


# Create your views here.
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render, render_to_response, redirect
from django.template import Context, RequestContext

def index(request):
    context = RequestContext(request, {
            'activate_navbar_element_id' : 'groups'
        })
    return render_to_response('groups/groups.html', context_instance=context)


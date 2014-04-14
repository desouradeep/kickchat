# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, render_to_response, redirect
from django.template import Context, RequestContext
from django.core.urlresolvers import reverse
from home import pagelets
import json
from random import randint

def create_payload(data):
    return_dict = {}
    pagelet_urls = {}
    ids = {}
    for key in data:
        id = str(randint(10**5, 10**6-1))
        pagelet_urls[id] = data[key]
        return_dict['ID_' + str(key)] = id
        ids['ID_' + str(key)] = id
    return_dict['pagelets'] = json.dumps(pagelet_urls)
    return_dict['count'] = len(pagelet_urls)
    return_dict['ids'] = json.dumps(ids)
    return return_dict


def index(request):
    template = 'home/home.html'
    return_dict = {}

    viewname_dict = {
        1: reverse('home-feed'),
        2: reverse('account_login'),
        3: reverse('account_signup'),
    }
    json_data = create_payload(viewname_dict)

    context = RequestContext(request, json_data)
    return render_to_response(template, context_instance=context)



def about(request):
    context = RequestContext(request, {
            'activate_navbar_element_id' : 'about'
    })
    return render_to_response('home/about.html', context_instance=context)
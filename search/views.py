from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, RequestContext
from django.template.response import TemplateResponse
from django.core.paginator import Paginator
from datetime import datetime
from ipdb import set_trace as st
from chat.models import message
from profiles.models import CustomUser

activated_navbar_element = 'search'

def index(request):
    if not request.user.is_authenticated():
        return redirect('/profile/register')
    user_not_found = False
    if request.GET.get('username'):
        CustomClient = CustomUser.objects.filter(username=request.GET.get('username'))
        if len(client) == 1:
            return redirect('/profile?username='+client[0].username)
        else:
            user_not_found = True
    context = RequestContext(request, {
        'activated_navbar_element': activated_navbar_element,
        'online' : '1',
        'current_user' : request.user,
        'user_not_found' : user_not_found,
            })
    return render_to_response('search/search.html',context_instance=context)
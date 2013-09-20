from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, RequestContext
from django.template.response import TemplateResponse
from django.core.paginator import Paginator
from datetime import datetime
from chat.models import message
from profiles.models import CustomUser
from django.contrib.auth.models import User

activated_navbar_element = 'search'

def index(request):
    if not request.user.is_authenticated():
        return redirect('/')
    user_not_found = False
    if request.method == 'POST':
        Client = User.objects.filter(username=request.POST['username'])
        if len(Client) == 1:
            return redirect('/profile/' + Client[0].username)
        else:
            user_not_found = True
    context = RequestContext(request, {
        'activated_navbar_element': activated_navbar_element,
        'request_user' : request.user,
        'user_not_found' : user_not_found,
            })
    return render_to_response('search/search.html',context_instance=context)

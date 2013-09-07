from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, RequestContext
from django.template.response import TemplateResponse
from django.core.paginator import Paginator
from datetime import datetime
from ipdb import set_trace as st
from chat.models import message
from profiles.models import user

activated_navbar_element = 'chat'

def index(request):
    if not request.user.is_authenticated():
        return redirect('/profile/login')
    
    if request.method == 'POST':
        time = datetime.now()
        msg = message(username=request.user.username,
                      time=datetime.now(),
                      message=request.POST['msg']
              )
        msg.save()

    messages = message.objects.all()
    users = user.objects.filter(is_online=True)
    context = RequestContext(request, {
        'msg' : messages,
        'users' : users,
        'activated_navbar_element': activated_navbar_element,
        'online' : '1',
        'current_user' : request.user,
            })
    return render_to_response('chat/chat.html', context_instance=context)

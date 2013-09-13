from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, RequestContext
from django.template.response import TemplateResponse
from django.core.paginator import Paginator
from datetime import datetime
from ipdb import set_trace as st
from chat.models import message
from profiles.models import CustomUser

activated_navbar_element = 'chat'

def index(request):
    if not request.user.is_authenticated():
        return redirect('/profile/register')
    
    if request.method == 'POST':
        time = datetime.now()
        msg = message(username=request.user.username,
                      time=datetime.now(),
                      message=request.POST['msg']
              )
        msg.save()

    messages = message.objects.all()
    online_users = CustomUser.objects.filter(is_online=True)
    current_user = CustomUser.objects.get(user=request.user)
    context = RequestContext(request, {
        'msg' : messages,
        'online_users' : online_users,
        'activated_navbar_element': activated_navbar_element,
        'online' : '1',
        'current_user' : current_user,
            })
    return render_to_response('chat/chat.html', context_instance=context)

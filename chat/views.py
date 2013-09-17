from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, RequestContext
from django.template.response import TemplateResponse
from django.core.paginator import Paginator
from datetime import datetime
from chat.models import message
from profiles.models import CustomUser

activated_navbar_element = 'chat'

def index(request):
    if not request.user.is_authenticated():
        return redirect('/profile/register')
    print request.is_ajax()
    if request.method == 'POST' and request.is_ajax():
        time = datetime.now()
        msg = message(username=request.user.username,
                      time=datetime.now(),
                      message=request.POST['message']
              )
        msg.save()
        return redirect('/chat')


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

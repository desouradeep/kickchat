from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, RequestContext
from django.template.response import TemplateResponse
from django.core.paginator import Paginator
from datetime import datetime

from chat.models import message
from profiles.models import user

activated_navbar_element = 'chat'

def index(request):
    if request.method == 'POST':
        time = datetime.now()
        msg = message(username='SDE',
                      time=datetime.now(),
                      message=request.POST['msg']
              )
        msg.save()

    messages = message.objects.all()
    context = RequestContext(request, {
        'msg' : messages,
        'activated_navbar_element': activated_navbar_element,
            })
    return render_to_response('chat/chat.html', context_instance=context)

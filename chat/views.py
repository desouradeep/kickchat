from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, RequestContext
from django.template.response import TemplateResponse
from django.core.paginator import Paginator
from datetime import datetime

from chat.models import user, message

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
            })
    return render_to_response('inner.html', context_instance=context)

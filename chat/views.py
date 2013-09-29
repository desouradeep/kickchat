from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, RequestContext
from django.template.response import TemplateResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
from chat.models import message
from profiles.models import CustomUser
from django.contrib.auth.models import User
import json
activated_navbar_element = 'chat'
import time
def index(request):
    if not request.user.is_authenticated():
        return redirect('/')

    # For message post
    if request.method == 'POST' and request.is_ajax():
        time = datetime.now()
        msg = message(username=request.user.username,
                      time=time,
                      message=request.POST['message']
              )
        msg.save()
        username = request.user.username
        time = msg.time.strftime('%b %d, %Y, %I:%M:%S %p')
        table_row = '''
           <tr id="%d">
             <td>
               <a href=\'/profile/%s\' target="blank"><b>%s</b></a>
             </td>
             <td>%s</td>
             <td style=\'font-size:10px;\'>%s</td>
           </tr>''' % (msg.id, msg.username, msg.username, msg.message, time)
        json_data = json.dumps({ 'table_row' : table_row , 'msg_id':msg.id})
        return HttpResponse(json_data, mimetype='application/json')

    elif request.method == 'GET' and request.is_ajax():

        # For show-more
        if request.GET.get('commit') == 'new_message':
            new = 30
            first = int(request.GET.get('first'))
            new_first = 0
            new_last = 0
            if first < new:
                new_last = first - 1
            else:
                new_first = first - new
                new_last = first
            messages = message.objects.all()[new_first:new_last]
            html_rows = ''
            for m in messages:
                time = m.time.strftime('%b %d, %Y, %I:%M:%S %p')
                html_rows += '''
                   <tr id="%d">
                     <td>
                       <a href=\'/profile/%s\' target="blank"><b>%s</b></a>
                      </td>
                     <td>%s</td>
                     <td style=\'font-size:10px;\'>%s</td>
                    </tr>''' % (m.id, m.username, m.username, m.message, time)
            disabled = False
            if new_first == 0:
                disabled = True
            json_data = json.dumps({'old_messages': html_rows, 'disabled': disabled})
            return HttpResponse(json_data, mimetype='application/json')

        # For auto-refresh
        elif request.GET.get('commit') == 'refresh' and request.is_ajax():
            last_id = int(request.GET.get('last_message'))
            if message.objects.count() > 0:
                latest_message = message.objects.latest('time')
            else:
                latest_message = []
            html_rows = ''
            if latest_message.id > last_id:
                messages = message.objects.all()[last_id:latest_message.id]
                for m in messages:
                    time = m.time.strftime('%b %d, %Y, %I:%M:%S %p')
                    html_rows += '''
                       <tr id="%d">
                         <td>
                           <a href=\'/profile/%s\' target="blank"><b>%s</b></a>
                         </td>
                         <td>%s</td>
                         <td style=\'font-size:10px;\'>%s</td>
                       </tr>''' % (m.id, m.username, m.username, m.message, time)
            json_data = json.dumps({'html_rows':html_rows})
            return HttpResponse(json_data, mimetype='application/json')

    messages = []
    if message.objects.count() > 0:
        latest_message = message.objects.latest('time')
        if latest_message.id > 31:
            messages = message.objects.all()[latest_message.id-30:latest_message.id]
        else:
            messages = message.objects.all()
    else:
        latest_message = []
    online_users = CustomUser.objects.filter(is_online=True)
    current_user = User.objects.get(username=request.user.username)
    context = RequestContext(request, {
        'msg' : messages,
        'online_users' : online_users,
        'activated_navbar_element': activated_navbar_element,
        'request_user' : request.user,
        })
    return render_to_response('chat/chat.html', context_instance=context)

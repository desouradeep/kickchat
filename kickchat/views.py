from django.shortcuts import render_to_response
from django.template import RequestContext


def about(request):
    context = RequestContext(request, {
        'activated_navbar_element' : 'about',
        })
    return render_to_response('about.html',context_instance=context)
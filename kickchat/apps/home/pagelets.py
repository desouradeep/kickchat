from django.http import HttpResponse

def feed(request):
    return HttpResponse('this is the feed')

def signin(request):
    return HttpResponse('signin template')

def register(request):
    return HttpResponse('register template')
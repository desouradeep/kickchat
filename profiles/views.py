from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate, logout, login
activated_navbar_element = 'profile'
from profiles.models import user

def login_user(request):
    if request.user.is_authenticated():
        return redirect('/profile')
    invalid = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
        # the password verified for the user
            if user.is_active:
                login(request, user)
                return redirect('/profile')
                auth = 'active'
                print("User is valid, active and authenticated")
        else:
            invalid = True
            # the authentication system was unable to verify the username and password
            print("The username and password were incorrect.")

    context = RequestContext(request, {
        'invalid' : invalid,
        'activated_navbar_element': activated_navbar_element,
       # 'user' : user,
            })
    #st()
    return render_to_response('profile/login.html',context_instance=context)

def logout_user(request):
    logout(request)
    return redirect('/profile')

def index(request):
    if not request.user.is_authenticated():
        return redirect('/profile/login')
    current_user = user.objects.get(username=request.user.username)
    context = RequestContext(request, {
        'activated_navbar_element': activated_navbar_element,
        'current_user' : current_user,  
        })
    return render_to_response('profile/profile.html', context_instance=context) 
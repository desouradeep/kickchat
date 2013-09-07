from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
activated_navbar_element = 'profile'
from profiles.models import user as user2
from ipdb import set_trace as st

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
                client = user2.objects.get(username=username)
                client.is_online = True
                client.save()
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
        'online' : '0',
            })
    #st()
    return render_to_response('profile/login.html',context_instance=context)

def logout_user(request):
    client = user2.objects.get(username=request.user.username)
    client.is_online = False
    client.save()
    logout(request)
    return redirect('/profile')

def index(request):
    if not request.user.is_authenticated():
        return redirect('/profile/login')
    current_user = user2.objects.get(username=request.user.username)
    context = RequestContext(request, {
        'activated_navbar_element': activated_navbar_element,
        'current_user' : current_user,
        'online' : '1'
        })
    return render_to_response('profile/profile.html', context_instance=context)

def register(request):
    if request.user.is_authenticated():
        return redirect('/profile')
    if request.method == 'POST':
        new_user = User.objects.create_user(
                username = request.POST['username'],
                email = request.POST['email_id'],
                password = request.POST['password'],
                )
        new_user.first_name = request.POST['first_name']
        new_user.last_name = request.POST['last_name']
        new_user.is_staff = False
        new_user.is_superuser = False
        
        new_user_basic = user2(
                username = request.POST['username'],
                roll_no = request.POST['roll_no'],
                fullname = (request.POST['first_name'] + ' ' + request.POST['last_name']),
                fb_profile = request.POST['fb_profile'],
                email_id = request.POST['email_id'],
            )
        new_user_basic.save()
        new_user.save()
        redirect('/profile')
    details = [
                {'Username': {'type':'text', 'name':'username'}},
                {'First Name': {'type':'text', 'name':'first_name'}},
                {'Last Name': {'type':'text', 'name':'last_name'}},
                {'Email': {'type':'email', 'name':'email_id'}},
                {'Password': {'type':'password', 'name':'password'}},
                {'Confirm Password': {'type':'password', 'name':'password2'}},
                {'Roll No.': {'type':'number', 'name':'roll_no'}},
                {'Facebook Profile': {'type':'url', 'name':'fb_profile'}},
    ]

    context = RequestContext(request, {
        'details' : details,
        'activated_navbar_element' : activated_navbar_element,
        'online' : '0',
        })
    return  render_to_response('profile/register.html',context_instance=context)
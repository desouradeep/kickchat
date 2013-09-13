from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
activated_navbar_element = 'profile'
from profiles.models import CustomUser
from ipdb import set_trace as st

def login_user(request):
    #if request.user.is_authenticated():
    #    return redirect('/profile')
    #invalid = ''
    print 2
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        request_user = authenticate(username=username, password=password)
        if request_user is not None:
        # the password verified for the user
            login(request, request_user)
            CustomClient = CustomUser.objects.get(user=request_user)
            CustomClient.is_online = True
            CustomClient.save()
            return True
        else:
            return False
    return False

def logout_user(request):
    CustomClient = CustomUser.objects.get(user=request.user)
    CustomClient.is_online = False
    CustomClient.save()
    logout(request)
    return redirect('/profile/register')

def index(request):
    if not request.user.is_authenticated():
        return redirect('/profile/register')
    current_user = CustomUser.objects.get(user=request.user)
    if request.GET.get('username'):
        auth_user = User.objects.get(username=request.GET.get('username'))
        query_user = CustomUser.objects.get(user=auth_user)
    else:
        query_user = current_user
    context = RequestContext(request, {
        'activated_navbar_element': activated_navbar_element,
        'current_user' : current_user,
        'query_user' : query_user,
        'online' : '1'
        })
    return render_to_response('profile/profile.html', context_instance=context)

def register(request):
    if request.user.is_authenticated():
        return redirect('/profile/')
    if request.method == 'POST':
        if request.POST['commit'] == 'Login':
            if login_user(request) == True:
                return redirect('/profile/')
            else:
                return redirect('/profile/register')

        duplicate_roll = CustomUser.objects.filter(roll_no=request.POST['roll_no'])
        duplicate_fb = CustomUser.objects.filter(fb_profile=request.POST['fb_profile'])
        if len(duplicate_fb) is 0 and len(duplicate_roll) is 0:
            new_user = User.objects.create_user(
                    username = request.POST['username'],
                    email = request.POST['email_id'],
                    password = request.POST['password'],
                    )
            new_user.first_name = request.POST['first_name']
            new_user.last_name = request.POST['last_name']
            new_user.is_staff = False
            new_user.is_superuser = False
            new_user.save()

            new_CustomUser = CustomUser(
                    user = new_user,
                    roll_no = request.POST['roll_no'],
                    fb_profile = request.POST['fb_profile'],
                    )
            new_CustomUser.is_online = True
            new_CustomUser.save()
            request_user = authenticate(username=request.POST['username'], 
                    password=request.POST['password'])
            login(request,request_user)
            return redirect('/chat')
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
        'activated_navbar_element' : 'Sign-Up',
        'online' : '0',
        })
    return render_to_response('profile/register.html',context_instance=context)
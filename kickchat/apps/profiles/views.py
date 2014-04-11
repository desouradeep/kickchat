from django.http import HttpResponse
from django.contrib.auth.models import User

from django.shortcuts import (render, render_to_response, redirect,
                              get_object_or_404)
from django.template import Context, RequestContext


def index(request, *args, **kwargs):
    if 'username' in kwargs:
        user = kwargs['username']
    else:
        user = request.user.username

    user_data = get_object_or_404(User, username=user)

    user_details = {
        'username': user_data.username,
        'fullname': user_data.first_name + ' ' + user_data.last_name,
        'email': user_data.email,
    }

    context = RequestContext(request, {
        'activate_navbar_element_id': 'profile',
        'user_details': user_details,
    })

    return render_to_response(
        'profiles/profiles.html',
        context_instance=context
    )

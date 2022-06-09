"""Users app views"""

from django.contrib.auth import get_user_model
from django.shortcuts import render

user = get_user_model

def login_view(request):
    return render(request , "users/login.html")

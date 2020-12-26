from typing import Reversible
from django.http.response import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        HttpResponseRedirect(Reversible("login"))
    return True
def login_view(request,session_id):
    return render(request,"layouts/users/login.html")
def logout_view(request,session_id):
    return True
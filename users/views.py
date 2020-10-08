from django.shortcuts import render,redirect
import django.http as http
from django.contrib.auth import authenticate,login
# Create your views here.


def login_views(request):
    if request.method == "POST":
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
    return render(request,'users/login.html')
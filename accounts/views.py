from django.shortcuts import render
from .models import User

def signup(request):
    if request.method=='Get':
        return render(request,'accounts/signup.html')
    else:

        return render(request,'accounts/signup.html')


def login(request):
    #if request.method=='Get':
    return render(request,'accounts/signup.html')


def logout(request):
    #if request.method=='Get':
    return render(request,'accounts/signup.html')

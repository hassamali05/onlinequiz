from django.shortcuts import render,redirect
from .models import User

def signup(request):
    if request.method=='GET':
        return render(request,'accounts/signup.html')
    else:
        username = request.POST['username']
        try:
            user = User.objects.get(name=username)
            return render(request,'accounts/signup.html',{'error':'User name already exists!'})
        except User.DoesNotExist:
            if request.POST['password1']==request.POST['password2']:
                newUser = User()
                newUser.name=username
                newUser.password=request.POST['password1']
                if request.POST['type']=='teacher':
                    newUser.type=1
                else:
                    newUser.type = 0
                newUser.address=request.POST['address']
                newUser.phone=request.POST['phone']
                newUser.save()
                return redirect('home')
            else:
                return render(request,'accounts/signup.html',{'error':'Password must be same'})


def login(request):
    if request.method=='GET':
        return render(request,'accounts/login.html')
    else:
        try:
            user = User.objects.get(name=request.POST['username'])
            if user.password == request.POST['password']:
                request.session['userID']=user.id
                if user.type==0:
                    return render(request,'students/student.html',{'user':user})
                else:
                    return render(request,'teachers/teacher.html',{'user':user})
            else:
                return render(request,'accounts/login.html',{'error':'User name or password is incorrect'})
        except User.DoesNotExist:
            return render(request,'accounts/login.html',{'error':'User name or password is incorrect'})


def logout(request):
    #if request.method=='Get':
    return render(request,'accounts/signup.html')

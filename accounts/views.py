from django.shortcuts import render, redirect
from .models import User
from teachers.models import Test


def signup(request):
    if request.method == 'GET':
        return render(request, 'accounts/signup.html')
    else:
        username = request.POST['username']
        try:
            user = User.objects.get(name=username)
            return render(request, 'accounts/signup.html', {'error': 'User name already exists!'})
        except User.DoesNotExist:
            if request.POST['password1'] == request.POST['password2']:
                new_user = User()
                new_user.name = username
                new_user.password = request.POST['password1']
                if request.POST['type'] == 'teacher':
                    new_user.type = 1
                else:
                    new_user.type = 0
                new_user.address = request.POST['address']
                new_user.phone = request.POST['phone']
                new_user.save()
                return redirect('home')
            else:
                return render(request, 'accounts/signup.html', {'error': 'Password must be same'})


def login(request):
    if request.method == 'GET':
        return render(request, 'accounts/login.html')
    else:
        try:
            user = User.objects.get(name=request.POST['username'])
            if user.password == request.POST['password']:
                request.session['userID'] = user.id
                if user.type == 0:
                    return render(request, 'students/student.html', {'user': user})
                else:
                    test = Test.objects.filter(teacher=user)
                    return render(request, 'teachers/teacher.html', {'user': user, "Test": test})
            else:
                return render(request, 'accounts/login.html', {'error': 'User name or password is incorrect'})
        except User.DoesNotExist:
            return render(request, 'accounts/login.html', {'error': 'User name or password is incorrect'})


def logout(request):
    del request.session['userID']
    request.session.flush()
    return redirect('login')

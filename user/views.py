from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import messages
from django. contrib.auth import authenticate,login as authorize, logout as deauth

# Create your views here.

def login(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        uname = request.POST['username']
        upwd  = request.POST['password']
        user = authenticate(username=uname,password=upwd)
        if user is None:
            messages.info(request, 'Please check credentials')
        else:
            # this will create the session for loged in user
            authorize(request,user)
            return redirect('/user/profile')
            # return HttpResponse('login ')
    else:
        if request.user.is_authenticated:
            return redirect('/user/profile')
    data = {'form':form,'title':'Login'}
    return render(request,'dj_login.html',data)

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            if form.save():
                messages.add_message(request,messages.SUCCESS,'User Succefully Registered')
                # return HttpResponse('messages',messages)
                # print(messages)
                return redirect('/user/login')
    data = {'title':'Register','form':form}
    # print(data)
    
    return render(request,'dj_register.html',data)

def profile(request):
    if request.user.is_authenticated:
        return render(request,'profile.html',data)
    else:
        messages.add_message(request,messages.INFO,'YOU have to login first')
        return redirect('/user/login')

    data = {'title':'Profile'}
    

def logout(request):
    if request.user.is_authenticated:
        deauth(request)
        messages.info(request,'You have succefully logged out')
        return redirect('/user/login')
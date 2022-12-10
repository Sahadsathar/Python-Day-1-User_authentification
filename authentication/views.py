from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):

    if request.method == 'post':
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password_1 = request.POST.get('password')
        password_2 = request.POST.get('pass2')
        username = request.POST.get('username')
        username = request.POST.get('username')
        myuser= User.objects.create_user(username,email, password_1)
        myuser_fname= firstname
        myuser_lname=lastname
        myuser.save()
        messages.success(request, "Your account has been successfully created")
        return redirect('signin')

    return render(request, 'signup.html')

def signin(request):
    return render(request, 'signin.html')

def signout(request):
    return render(request, 'signout.html')
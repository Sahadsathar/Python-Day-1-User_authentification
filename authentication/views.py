from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from user_login_system import settings
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password_1 = request.POST.get('password')
        password_2 = request.POST.get('pass2')

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist. Use another user name")
            return redirect('home')
        # if User.objects.filter(email=email):
        #     messages.error(request, "Email already exist. Use another Email")
        #     return redirect('home')
        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters")
        if password_1 != password_2:
            messages.error(request, "passwords didn't match")

        myuser = User.objects.create_user(username, email, password_1)
        myuser.fname = firstname
        myuser.lname = lastname
        myuser.save()
        messages.success(request, "Your account has been successfully created. We have sent you confirmation email, please confirm your email inorder to activate account")
        return redirect('signin')

        subject = "Welcome to the Sahad World"
        message = "Hello" + User.first_name + "!! \n Welcome.\n Please confirm your email address to activate account \n thanking " \
                                              "you "
        from_email = settings.EMAIL_HOST_USER
        to_email = [myuser.email]
        send_mail(subject,message, from_email,to_email, fail_silently=False)

    return render(request, 'signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            name = user.username
            return render(request, 'home.html', {'name': name})
        else:
            messages.error(request, 'Bad credentials!!')
            return redirect('signin')
    return render(request, 'signin.html')


def signout(request):
    return render(request, 'signout.html')

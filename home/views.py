from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from passlib.hash import pbkdf2_sha256
from django.core.files.storage import FileSystemStorage
# Create your views here.

def home(request):
    return render(request, 'index.html')

def signin(request) :
    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None :
            login(request, user)
            fname = user.first_name
            return render(request, 'folder.html', {'name': fname})

        else :
            messages.error(request,"Incoorect Username and password")
            return redirect('signin')
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        print(uploaded_file.name)
        print(uploaded_file.size)
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
    
    return render(request, 'signin.html')

def forgot(request) :
    return render(request, 'forgot.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # enc_password = pbkdf2_sha256.encrypt(pass1,rounds=12000,salt_size=32)

        if len(username) > 10 :
            messages.error(request, "Username length must be less than or equal to 10 charcter")
            return redirect('signup')
        if len(pass1) < 8 :
            messages.error(request, "password length must be less than or equal to 8 charcter")
            return redirect('signup')
        if not pass1.isalnum() :
            message.error(request, "password must contain alnum") 
        if pass1 != pass2 :
            messages.error(request, "Password do not match")
            return redirect('signup')
        if not username.isalnum() :
            messages.error(request, "Useranem must be alnum")
            return

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.password = pass1
        myuser.save()
        return redirect('signin')
    return render(request, 'signup.html')


def folder(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        print(uploaded_file.name)
        print(uploaded_file.size)
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
    return render(request, 'folder.html')

def signout(request) :
    logout(request)
    messages.error(request, "Looged out succesfully")
    return redirect('home')



    
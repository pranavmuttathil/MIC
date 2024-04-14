from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from .models import Person
from .forms import RegistrationForm,LoginForm # Creating Views


def index(request):
    return render(request, 'index.html')

def register(request):
    #Getting the Form Data
    form = RegistrationForm()
    
    if (request.method=="POST"):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            name = cleaned_data["name"]
            email = cleaned_data["email"]
            password = cleaned_data["password"]
            confirm_password = cleaned_data["confirm_password"]
            
            #Checking for Validity of Data
            if password != confirm_password:
                messages.error("Passwords do not match")
            if '@' not in email:
                return "Enter a valid Gmail" 
            if name > 24 or name < 2:
                messages.error(request, 'Invalid Name')
            if not Person.objects.filter(name=name).exists():
                messages.error(request, 'Username already taken')
            if password > 24:
                messages.error("Invalid Password")
                 
            #Creating a User
            hashed_password = make_password(password)
            user = Person.objects.create(name=name,email=email,password=password,confirm_password=confirm_password)
            #Saving Data to Database
            savedata = Person(name=name,email=email,password=password,confirm_password=confirm_password)
            savedata.save()  
            messages.success("User Has been Created")    
        return redirect('login/')
    return render(request,'register_view.html', {"form":form})

def login(request):
    form1 = LoginForm(request.POST)
    if form1.is_valid:
        name1 = form1.cleaned_data["name1"]
        password1 = form1.cleaned_data["password1"]
        user1 = authenticate(name=name1, password=password1)
        if user1 is None:
            messages.error(request, "Invalid Password")
            return redirect('/login/')
        else:
            login(request, user1)
            return redirect('/home/')

    return render(request, "login_view.html")
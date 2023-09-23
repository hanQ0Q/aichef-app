from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import User
# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    return render(request, "users/user.html")

def signup_view(request):
    if request.method == "GET":
        return render(request, "users/signup.html")
    
    if request.method == "POST":
        email = request.POST["email"]
        mobile = request.POST["mobile"]
        password = request.POST["password"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        if User.objects.filter(email=email).exists():
            return render(request, "users/signup.html", {
                "message":"User already exists for this email."
            })
        if User.objects.filter(mobile=mobile).exists():
            return render(request, "users/signup.html", {
                "message":"User already exists fot this mobile."
            })
        user = User.objects.create_user(username=email, email=email, password=password, mobile=mobile, 
                                        first_name = first_name, last_name = last_name,
                                        ) 
        user.save()
        return render(request, "users/login.html", {
                "message":"Account created. Please use your email and password to log in."
            })

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("users:index"))
        else:
            return render(request, "users/login.html", {
                "message":"Invalid credentials."
            })

    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {
        "message": "Logged out."
    })
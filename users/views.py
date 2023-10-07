import uuid
import logging

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import get_user_model, login


from .models import User
from recipes.models import Recipe
from food.models import UserFoodItem
# Create your views here.

logger = logging.getLogger('aichef')

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    recipes = Recipe.objects.filter(user=request.user).order_by('-recipe_date')[:3]
    user_foods = UserFoodItem.objects.filter(user=request.user)
    context = {
        "recipes": recipes,
        'user_foods': user_foods,
    }
    return render(request, "users/user.html", context=context)

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
                "message":"🎉🎉🎉 Congratulations! Your account created! Now you use your email and password to log in."
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

def guest_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:index"))

    user = get_user_model().objects.create(username=uuid.uuid4(), is_guest=True, first_name="Guest", last_name="")
    user.set_unusable_password()
    user.save()
    login(request, user)
    logger.info(f"user: {request.user}")
    return HttpResponseRedirect(reverse("users:index"))
    

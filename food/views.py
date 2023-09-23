import logging
from django.shortcuts import render, get_object_or_404
from .models import FoodCategory, FoodItem, UserFoodItem
from django.http import HttpResponseRedirect
from django.urls import reverse

logger = logging.getLogger('aichef')

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))


    food_category = FoodCategory.objects.all()
    user_foods = UserFoodItem.objects.filter(user=request.user)
    food_data = {}
    for category in food_category:
        food_data[category.name] = list(FoodItem.objects.filter(category=category).values_list("name", flat=True))

    logger.info(f"food_data:  {food_data}")
    data = {
        'foods': food_data,
        'user_foods': user_foods,
    }
    return render(request, "food/food.html", context=data)

def add(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    if request.method == "POST":
        selected_item = request.POST.get('selectedItem')
        item = FoodItem.objects.get(name=selected_item)
        if UserFoodItem.objects.filter(item=item, user=request.user).exists():
            return HttpResponseRedirect(reverse("food:index"))
        user_food = UserFoodItem.objects.create(item=item, user=request.user)
        user_food.save()
        return HttpResponseRedirect(reverse("food:index"))
    

def delete(request, food_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    
    food = FoodItem.objects.get(id=food_id)
    if UserFoodItem.objects.filter(item=food, user=request.user).exists():
        UserFoodItem.objects.get(item=food, user=request.user).delete()

    return HttpResponseRedirect(reverse("food:index"))
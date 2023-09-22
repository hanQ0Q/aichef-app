from django.shortcuts import render
from .models import FoodCategory, FoodItem, UserFoodItem
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    food_category = FoodCategory.objects.all()
    food_data = {}
    for category in food_category:
        food_data[category.name] = list(FoodItem.objects.filter(category=category).values_list("name"))

    print(f"food_data:  {food_data}")
    context = {
        'foods': food_data
    }
    return render(request, "food/food.html", context=context)
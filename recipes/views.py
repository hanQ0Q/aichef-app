import logging
from django.shortcuts import render

from .models import Recipe
from food.models import UserFoodItem
from django.http import HttpResponseRedirect
from django.urls import reverse
from .cgpt import get_recipe, get_separate_recipe


logger = logging.getLogger('aichef')


ERROR_MESSAGES = {
    "NO_ITEMS": "No food items available for users",

}
IS_ERROR_MESSAGE: bool = False
ERROR_NAME = ""


# Create your views here.
def index(request):
    global IS_ERROR_MESSAGE, ERROR_NAME
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    recipes = Recipe.objects.filter(user=request.user)
    context = {
        "recipes": recipes
    }
    if IS_ERROR_MESSAGE:
        IS_ERROR_MESSAGE = False
        context["message"] = ERROR_MESSAGES.get(ERROR_NAME, "")
    return render(request, "recipes/recipes.html", context=context)


def create_recipe(request):
    global IS_ERROR_MESSAGE, ERROR_NAME
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("users:login"))
    if request.method == "POST":
        breakfast = request.POST.get("breakfast")
        lunch = request.POST.get("lunch")
        dinner = request.POST.get("dinner")
        recipe = Recipe.objects.create(
            instruction=breakfast,
            meal_type="BR",
            user=request.user,
        )
        recipe.save()
        recipe = Recipe.objects.create(
            instruction=lunch,
            meal_type="LC",
            user=request.user,
        )
        recipe.save()
        recipe = Recipe.objects.create(
            instruction=dinner,
            meal_type="DN",
            user=request.user,
        )
        recipe.save()
        return HttpResponseRedirect(reverse("recipes:index"))
    items = list(UserFoodItem.objects.filter(user=request.user).values_list("item__name", flat=True))

    if not items:
        IS_ERROR_MESSAGE = True
        ERROR_NAME = "NO_ITEMS"
        return HttpResponseRedirect(reverse("recipes:index"))

    recipe = get_recipe(items)
    recipe_data = get_separate_recipe(recipe)
    logger.info("Recipe created successfully.")
    context = {
        "recipe": recipe_data
    }
    return render(request, "recipes/new_recipe.html", context=context)



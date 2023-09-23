from django.shortcuts import render
from .models import Recipe
from food.models import UserFoodItem
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
import openai
from openai.error import RateLimitError

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
        print(f"##################################     {breakfast}")
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
    print(f"items:---------------------{items}")
    recipe = get_recipe(items)
    recipe_data = get_separate_recipe(recipe)
    print(f"Recipe>>>>>>>>>>>>>>>>>>>>>>>>>{recipe_data}")
    if not items:
        IS_ERROR_MESSAGE = True
        ERROR_NAME = "NO_ITEMS"
        return HttpResponseRedirect(reverse("recipes:index"))
    context = {
        "recipe": recipe_data
    }
    return render(request, "recipes/new_recipe.html", context=context)


def get_recipe(ingredients):
    try:
        openai.api_key = settings.OPEN_AI_KEY
        prompt = f"I have the following ingredients: {ingredients}. Kindly provide recipe for 3 meals i.e. breakfast " \
                 f"lunch and dinner ? Add title to the recipe in following format 'Breakfast:'",
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=600
        )
        return response.choices[0].text
    except RateLimitError:
        print(f"Recharge your account: {RateLimitError.user_message}")


def get_separate_recipe(res: str):
    recipe_string = res
    # Separate recipes based on titles
    breakfast_marker = "Breakfast:"
    lunch_marker = "Lunch:"
    dinner_marker = "Dinner:"

    breakfast_start = recipe_string.find(breakfast_marker)
    lunch_start = recipe_string.find(lunch_marker)
    dinner_start = recipe_string.find(dinner_marker)

    breakfast_recipe: str = None
    lunch_recipe: str = None
    dinner_recipe: str = None

    if breakfast_start != -1:
        if lunch_start != -1:
            breakfast_recipe = recipe_string[breakfast_start:lunch_start].strip()
        elif dinner_start != -1:
            breakfast_recipe = recipe_string[breakfast_start:dinner_start].strip()
        else:
            breakfast_recipe = recipe_string[breakfast_start:].strip()

    if lunch_start != -1:
        if dinner_start != -1:
            lunch_recipe = recipe_string[lunch_start:dinner_start].strip()
        else:
            lunch_recipe = recipe_string[lunch_start:].strip()

    if dinner_start != -1:
        dinner_recipe = recipe_string[dinner_start:].strip()
    return {
        "breakfast": breakfast_recipe,
        "lunch": lunch_recipe,
        "dinner": dinner_recipe
    }
    # print("Breakfast Recipe:")
    # print(breakfast_recipe)
    # print("\nLunch Recipe:")
    # print(lunch_recipe)
    # print("\nDinner Recipe:")
    # print(dinner_recipe)
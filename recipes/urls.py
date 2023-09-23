from django.urls import path
from . import views
app_name = "recipes"
urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.create_recipe, name="create-recipe"),
   
]
from django.urls import path
from . import views
app_name = 'food'
urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add"),
    path("delete/<int:food_id>", views.delete, name="delete"),
    
]
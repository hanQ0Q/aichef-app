from django.contrib import admin

from .models import FoodCategory, FoodItem, UserFoodItem

# Register your models here.
class FoodCategoryAdmin(admin.ModelAdmin):
    list_dispaly = ("id", "name")

class FoodItemAdmin(admin.ModelAdmin):
    list_dispaly = ("id", "name", "category", "calorie","protein","food_type","user") 

class UserFoodItemAdmin(admin.ModelAdmin):
    list_dispaly = ("id", "item", "user", "expiry", "purchased_on")

admin.site.register(FoodCategory, FoodCategoryAdmin)
admin.site.register(FoodItem, FoodItemAdmin)
admin.site.register(UserFoodItem, UserFoodItemAdmin)
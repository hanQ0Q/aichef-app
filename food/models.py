from django.db import models
from users.models import User



# Create your models here.

class FoodCategory(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name="name")
   

    def __str__(self) -> str:
        return f"{self.id} - {self.name}"
    
class FoodItem(models.Model):
    GENERIC = "GEN"
    CUSTOM = "CUS"
    FOOD_TYPE_CHOICES = (
        (GENERIC, "generic"),
        (CUSTOM, "custom"),
    )
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name="name")
    category = models.ForeignKey(FoodCategory, null=True, blank=True, related_name="food_items", on_delete=models.CASCADE,verbose_name="category")
    calorie = models.PositiveIntegerField( blank=True, null=True, verbose_name="calorie")
    protein = models.PositiveIntegerField( blank=True, null=True, verbose_name="protein")
    food_type = models.CharField(max_length=3, choices=FOOD_TYPE_CHOICES, blank=True, null=True, verbose_name="food type")
    user =  models.ForeignKey(User, null=True, blank=True, related_name="food_items", on_delete=models.CASCADE,verbose_name="user")
   

    def __str__(self) -> str:
        return f"{self.id} - {self.name}"
    
class UserFoodItem(models.Model):
    item = models.ForeignKey(FoodItem, null=True, blank=True,on_delete=models.CASCADE, related_name="user_food_items", verbose_name="item")
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="user_food_items", verbose_name="user")
    expiry = models.DateField(blank=True, null=True, verbose_name="expiry")
    purchased_on = models.DateField(blank=True, null=True, verbose_name="purchased on")
    
    def __str__(self) -> str:
        return f"{self.id} - {self.user} {self.item} "
    
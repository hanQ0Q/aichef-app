from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(max_length=50, blank=True, null=True, verbose_name="first name")
    last_name = models.CharField(max_length=50, blank=True, null=True, verbose_name="last name")
    email = models.EmailField(verbose_name="email")
    password = models.CharField(max_length=50, verbose_name="password")
    mobile = models.CharField(max_length=10)
    is_guest = models.BooleanField(default=False, verbose_name="is guest")


    def __str__(self) -> str:
        return f"{self.id} - {self.first_name} {self.last_name}"
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
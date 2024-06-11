from django.db import models
from django.contrib.auth.models import User

class Menu(models.Model):
    day_of_week = models.CharField(max_length=10)
    food_item = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.day_of_week}: {self.food_item}"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    order_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.menu.food_item} on {self.order_date}"



# from django.db import models

# # Create your models here.

from django.contrib import admin
from .models import Dish, Order

# Register your models here.
admin.site.register(Dish)
admin.site.register(Order)
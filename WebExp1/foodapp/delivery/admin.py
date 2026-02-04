from django.contrib import admin
from .models import Order #our app is delivery and we are importing Order[database] model from models.py file of delivery app

# Register your models here.
admin.site.register(Order)
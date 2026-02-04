# Ex02 Django ORM Web Application

## Date: 03-03-2026

## AIM
To develop a Django application to manage an online food delivery platform like Zomato/Swiggy using Object Relational Mapping (ORM).

## ENTITY RELATIONSHIP DIAGRAM

![alt text](<Screenshot 2026-02-04 072848.png>)


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM

models.py
`
from django.db import models

# Create your models here.

class Order(models.Model):
    order_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    order_date = models.DateTimeField()
    delivery_address = models.CharField()
    item_name = models.CharField(max_length=100)
    unit_price = models.DecimalField(max_digits=8, decimal_places=2)
    order_qty = models.IntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order {self.order_id} by User {self.user_id}"
`
admin.py
`
from django.contrib import admin
from .models import Order #our app is delivery and we are importing Order[database] model from models.py file of delivery app

# Register your models here.
admin.site.register(Order)
`

## OUTPUT

Include the screenshot of your admin page.

![alt text](<Screenshot 2026-02-04 065427.png>)

![alt text](<Screenshot 2026-02-04 065516.png>)

![alt text](<Screenshot 2026-02-04 065534.png>)



## RESULT
Thus the program for creating a database using ORM has been executed successfully

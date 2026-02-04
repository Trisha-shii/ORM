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
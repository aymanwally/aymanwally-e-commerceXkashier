from django.db import models

# Create your models here.


class Orders(models.Model):
    IN_CART = 0
    CHECKOUT_STARTED = 1
    PAYMENT_PENDING = 2
    PAYMENT_FAIL = 3
    PAYMENT_SUCCESS = 4
    ORDER_STATUS = (
        (IN_CART, "IN_CART"),
        (CHECKOUT_STARTED, "CHECKOUT_STARTED"),
        (PAYMENT_PENDING, "PAYMENT_PENDING"),
        (PAYMENT_FAIL, "PAYMENT_FAIL"),
        (PAYMENT_SUCCESS, "PAYMENT_SUCCESS"),
    )
    price = models.IntegerField(null=True, blank=True, default=1500)
    quantity = models.IntegerField(null=True, blank=True)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    phone_number = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    customer_identifier = models.CharField(max_length=255, blank=True)
    status = models.IntegerField(choices=ORDER_STATUS, default=IN_CART)

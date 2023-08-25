from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.views import View
from ecommerce.models import Orders

class OrderView(View):
    def get(self , request):
        products = [{
            "name": "test_product",
            "price": 1500,
            "desc": "test product for checkout"
        }]
        return render(request, 'order.html', {'products': products})
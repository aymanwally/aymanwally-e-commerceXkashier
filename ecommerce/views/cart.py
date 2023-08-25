from django.shortcuts import render , redirect

from django.contrib.auth.hashers import  check_password
from django.views import  View
from ecommerce.models import Orders
class Cart(View):
    def get(self , request):
        order = Orders.objects.get(customer_identifier=request.GET.get('order'))
        return render(request, 'cart.html', {'order': order})
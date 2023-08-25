from django.shortcuts import render, redirect, reverse

from django.contrib.auth.hashers import check_password
from django.views import View
from ecommerce.models import Orders


class CheckOut(View):
    def post(self, request):
        order = Orders(customer_identifier=request.POST.get('csrfmiddlewaretoken'))
        order.save()
        url = reverse('cart')
        redirect_to = url + '?order='+request.POST.get('csrfmiddlewaretoken')
        return redirect(redirect_to)
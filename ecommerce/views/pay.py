from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.views import View
from ecommerce.models import Orders
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator



import hmac
import hashlib
import binascii

MERCHANT_ID = "MID-21191-837"
import string
import random

# initializing size of string
N = 7

# using random.choices()
# generating random strings


def get_order_id(order):
    return "A%s".zfill(6) % order.id

def generateKashierOrderHash(order):
    path = '/?payment={}.{}.{}.{}'.format(MERCHANT_ID, get_order_id(order), 1500, "EGP")
    path = bytes(path, 'utf-8')
    secret = "41ca3e15-f2d6-44a2-b6b0-90717ea098c3"
    secret = bytes(secret, 'utf-8')
    return hmac.new(secret, path, hashlib.sha256).hexdigest()


class PayView(View):
    def post(self , request):
        print(request.POST.get('csrfmiddlewaretoken'))
        order = Orders.objects.get(customer_identifier=request.POST.get('customer_id'))
        order.first_name = request.POST.get('first_name')
        order.last_name = request.POST.get('last_name')
        order.phone_number = request.POST.get('phone')
        order.email = request.POST.get('email')
        order.status = Orders.PAYMENT_PENDING
        order.save()

        payment_url = (
            "https://checkout.kashier.io/?merchantId={mid}&orderId={order_id}&amount=1500&currency=EGP&hash={ohash}&mode=test&"
            "merchantRedirect={success_url}&"
            "serverWebhook={callback_url}&"
            "paymentRequestId={order_customer_id}&"
            "failureRedirect={failure_url}&"
            "redirectMethod=post&"
            "display=en"
        ).format(mid=MERCHANT_ID,
                 ohash=generateKashierOrderHash(order),
                 order_id=get_order_id(order),
                 success_url="https://webhook.site/8e3c3008-d192-41da-982f-2db731c13502",
                 callback_url="https://webhook.site/8e3c3008-d192-41da-982f-2db731c13502",
                 failure_url="https://webhook.site/8e3c3008-d192-41da-982f-2db731c13502",
                 order_customer_id=order.customer_identifier)
        return redirect(payment_url)

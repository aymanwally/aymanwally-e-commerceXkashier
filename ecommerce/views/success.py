from django.views import  View
from ecommerce.models import Orders
from django.shortcuts import render , redirect
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
import requests
import json


def create_invoice(order_id):

    url = "https://test-api.kashier.io/paymentRequest/?currency=EGP"

    payload = json.dumps({
    "paymentType": "professional",
    "merchantId": "MID-21191-837",
    "customerName": "test customer",
    "dueDate": "2023-08-31T10:49:24.831Z",
    "isSuspendedPayment": True,
    "description": "some description",
    "invoiceReferenceId": "000A{}".format(order_id.id),
    "invoiceItems": [
        {
        "description": "test order",
        "quantity": 1,
        "itemName": "laptop",
        "unitPrice": order_id.price,
        "subTotal": 1500
        }
    ],
    "state": "submitted",
    "currency": "EGP",
    "extraFees": [
        {
        "name": "xxx",
        "rate": 100,
        "flatFee": 100
        }
    ]
    })
    headers = {
    'Authorization': '9228f472c974eb545b24d0645b3931b3$32f2242df1584c5210aecc8fee3aceba3e1fcfba89e25443bf6414e9f832167d8b14bf7e6871040b6bb0b2c57e679bc0',
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    data = response.json()
    inv = data['response']['paymentRequestId']
    return inv

def send_invoice(INV, order_id):
    url = "https://test-api.kashier.io/paymentRequest/sendInvoiceBy?operation=share_payment_Request&currency=EGP"

    payload = json.dumps({
    "subDomainUrl": "http://merchant.kashier.io/en/prepay",
    "urlIdentifier": INV,
    "customerName": "test customer",
    "storeName": "TEST ft- MK Company",
    "customerPhoneNumber": order_id.phone_number,
    "language": "en",
    "operation": "phone"
    })
    headers = {
    'Authorization': '5b50e9ef95e8695f2dda0a16db717ce0$4188f97b6c5d5acf5bbc90443d9bef3c0b254dbc5309b8f9f15f003858ba6b206734466431a0aaace1a58d239b270cee',
    'Content-Type': 'application/json',
    'Cookie': '7bcf06c8cf5e7c2bc61ad0bfe7c28d07=1db7a40a831dfa0e3ac801da009b800c'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)

@method_decorator(csrf_exempt, name='dispatch')
class SuccessView(View):
    def post(self, request):
        # data = request.POST
        data = json.loads(request.body.decode('utf-8'))
        print(data)
        status = data["data"]["status"]
        order_id = data["data"]["merchantOrderId"]
        morder = order_id.split("A")[1]
        o = Orders.objects.get(id=morder)
        if status == "SUCCESS":
            o.status = Orders.PAYMENT_SUCCESS
            o.save()
        else:
            o.status = Orders.PAYMENT_FAIL
            o.save()
            inv = create_invoice(o)
            w = send_invoice(inv, o)
        return render(request, 'status.html', {'order': o})
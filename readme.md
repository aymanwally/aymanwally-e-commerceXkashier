# Introduction

The goal of this project is to integrate kashir payment Getway to a simple e-Commerce platform with updating the order status and sending invoice link to the customer if the iframe transaction fails
this project written with django 4 and python 3.

### Main features

- Django Admin Ecommerce
- Kashier Payment Method Simulator
- Easy navigation
- Checkout page
- reciept redirection

# Usage
The System is created to simulate a transcation using Kashier Payment method, Where one static product was created on a backend level, where by choosing the product it fetches the payment URL, and simulates a transaction and then it updates the status on the backend. 

In case the transaction was declined, the system will send an invoice to the customer an invoice with the number in the billing data. 

### Existing virtualenv

If your project is already in an existing python3 virtualenv first install django by running

    $ pip install django

If you haven't install requests library

    $ pip install requests
    
And then run the `manage.py` command to start the new project:

    $ python manage.py runserver

### creating virtualenv
installing the virtual environment

    $ pip install virtualenv

create a new virtual environment named env
      
    $ python -m venv env 


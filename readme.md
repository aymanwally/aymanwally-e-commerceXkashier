# Introduction

The goal of this project is to integrate kashir payment Getway to a simple e-Commerce platform with updating the order status and sending invoice link to the customer if the iframe transaction fails
this project written with django 4 and python 3.

![Default Home View](__screenshots/cart.png?raw=true "Title")

### Main features

- Django Admin Ecommerce
- Kashier Payment Method Simulator
- Easy navigation
- Checkout page
- reciept redirection

# Usage
The System is created to simulate a transcation using Kashier Payment method, Where one static product was is created on a backend level, where by choosing the product it fetches the payment URL, and simulates a transaction and then it updates the status on the backend. 

In case the transaction was declined, the system will send an invoice to the customer an invoice with the number in the billing data. 

### Existing virtualenv

If your project is already in an existing python3 virtualenv first install django by running

    $ pip install django
    
And then run the `django-admin.py` command to start the new project:

    $ django-admin.py startproject \
      --template=https://github.com/nikola-k/django-template/zipball/master \
      --extension=py,md \
      <project_name>
      
### No virtualenv

This assumes that `python3` is linked to valid installation of python 3 and that `pip` is installed and `pip3`is valid
for installing python 3 packages.

Installing inside virtualenv is recommended, however you can start your project without virtualenv too.

If you don't have django installed for python 3 then run:

    $ pip3 install django
    
And then:

    $ python3 -m django startproject \
      --template=https://github.com/nikola-k/django-template/zipball/master \
      --extension=py,md \
      <project_name>
      
      
After that just install the local dependencies, run migrations, and start the server.

{% endif %}

# {{ project_name|title }}

# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone git@github.com/USERNAME/{{ project_name }}.git
    $ cd {{ project_name }}
    
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install -r requirements/local.txt
    
    
Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver

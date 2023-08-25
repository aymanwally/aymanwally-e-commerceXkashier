"""
URL configuration for aymancommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path  , include
from django.conf.urls.static import static
from ecommerce.views.cart import Cart
from ecommerce.views.checkout import CheckOut
from ecommerce.views.orders import OrderView
from ecommerce.views.pay import PayView
from ecommerce.views.success import SuccessView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart', Cart.as_view(), name='cart'),
    path('checkout', CheckOut.as_view(), name='checkout'),
    path('pay', PayView.as_view(), name='pay'),
    path('success', SuccessView.as_view(), name='success'),
    path('', OrderView.as_view(), name='orders'),   
]

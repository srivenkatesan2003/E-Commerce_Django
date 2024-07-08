"""
URL configuration for New_Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.urls import path
from .views import *

urlpatterns = [
    path('all/customers/',customerlist),
    path('add/customers/',customeradd),
    path('delete/customers/<int:id>/',customer_delete, name='customer_delete'),
    path('update/customers/<int:id>/',customer_update, name='customer_update'),
    path('add/orders/', OrdersAdd),
    path('orders/', OrdersList),
    path('delete/order/<int:id>/',OrderDelete ,name='order_delete'),
    path('update/order/<int:id>/',OrderUpdate ,name='order_update'),

]
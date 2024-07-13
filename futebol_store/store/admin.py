from django.contrib import admin

from .models import Client
from .models import Order
from .models import OrderItem
from .models import Payment


admin.site.register(Client)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Payment)

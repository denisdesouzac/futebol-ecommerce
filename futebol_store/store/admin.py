from django.contrib import admin

from .models import Client, Order, OrderItem, Payment

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'unit_price', 'total_price')
    readonly_fields = ('unit_price', 'total_price')
    
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_date', 'status', 'client', 'delivery_address')
    readonly_fields = ('delivery_address',)
    
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('order', 'value', 'payment_date', 'payment_method')
    readonly_fields = ('value',)

admin.site.register(Client)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Payment, PaymentAdmin)

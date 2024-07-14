from django.db import models
from django.contrib.auth.models import User
from catalog.models import Product

# Representa os clientes e administradores.
class Client(models.Model):
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)  # ajustando o tamanho máximo para 15, considerando códigos de país
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Usuário deve ser único para cada cliente

    def __str__(self):
        return self.user.username


# Representa os pedidos realizados pelos clientes.
class Order(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('shipped', 'Shipped'), ('delivered', 'Delivered'), ('cancelled', 'Cancelled')])
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='orders')
    delivery_address = models.CharField(max_length=200, blank=True)

    def save(self, *args, **kwargs):
        if not self.delivery_address:
            self.delivery_address = self.client.address  # Assumindo que o modelo Client possui um campo `address`
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order {self.id} by {self.client.user.username}"

# Representa os produtos contidos em um pedido.
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def save(self, *args, **kwargs):
        self.unit_price = self.product.price
        self.total_price = self.unit_price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Order {self.order.id}"

# Representa as informações de pagamento dos pedidos.
class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='payments')
    value = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=20, choices=[('credit_card', 'Credit Card'), ('boleto', 'Boleto'), ('pix', 'Pix')])

    def save(self, *args, **kwargs):
        if not self.value:
            self.value = sum(item.total_price for item in self.order.order_items.all())
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Payment of {self.value} for Order {self.order.id}"

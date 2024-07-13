from django.db import models

# Representa as categorias de produtos.
class Category(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(max_length=200)  # Usando TextField para descrições mais longas

    def __str__(self):
        return self.name

# Representa os produtos disponíveis na loja.
class Product(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Usando DecimalField para precisão de preços
    quantity_in_stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name

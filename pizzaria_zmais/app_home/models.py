from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class PizzaModel(models.Model):
    pizza = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    imagem = models.URLField()
    ingredientes = models.TextField()

    criado_em = models.DateTimeField(auto_now_add=True)
    alterado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Pizza({self.pizza}, {self.preco}, {self.ingredientes})"
    
class VendaModel(models.Model):
    criado_em = models.DateTimeField(auto_now_add=True)
    alterado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Venda({self.criado_em}, {self.alterado_em})"

class VendaPizzaModel(models.Model):
    pizza = models.ForeignKey(PizzaModel, on_delete=models.CASCADE)
    venda = models.ForeignKey(VendaModel, on_delete=models.CASCADE)
    preco = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"VendaPizza({self.pizza}, {self.venda}, {self.preco})"
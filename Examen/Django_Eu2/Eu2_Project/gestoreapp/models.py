from django.db import models
from webapp.models import Producto, Cliente
# Create your models here.
class DetallePedido(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido = models.ForeignKey('Pedido', on_delete=models.CASCADE)
    cantidad = models.IntegerField()

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    
    fecha=models.DateField()

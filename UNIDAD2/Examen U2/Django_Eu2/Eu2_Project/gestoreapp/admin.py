from django.contrib import admin
from gestoreapp.models import DetallePedido, Pedido
from webapp.models import Producto, Categoria, Cliente

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(DetallePedido)
admin.site.register(Pedido)
from django.contrib import admin
from webapp.models import Cliente, Categoria, Producto

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Categoria)
admin.site.register(Producto)

from django.forms import ModelForm,EmailInput
from webapp.models import Producto, Cliente, Categoria

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'email': EmailInput(attrs={'type':'email'})
        }


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'email': EmailInput(attrs={'type':'email'})
        }

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'
        widgets = {
            'email': EmailInput(attrs={'type':'email'})
        }
from django.forms import ModelForm,EmailInput
from gestorapp.models import DetallePedido, Pedido

class DetallePedidoForm(ModelForm):
    class Meta:
        model = DetallePedido
        fields = '__all__'
        widgets = {
            'email': EmailInput(attrs={'type':'email'})
        }

class PedidoForm(ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'
        widgets = {
            'email': EmailInput(attrs={'type':'email'})
        }


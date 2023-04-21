from django.shortcuts import render, redirect, get_object_or_404
from gestorapp.models import Pedido, DetallePedido
from gestorapp.forms import PedidoForm, DetallePedidoForm

#CRUD pacientes
def detallePedido(request,id):
    pedido = get_object_or_404(Pedido,pk=id)
    return render(request,'detallePedido.html',{'pedido':pedido})

def nuevoPedido(request):
    if request.method == "POST":
        formaPedido = PedidoForm(request.POST)
        if formaPedido.is_valid():
            formaPedido.save()
            return redirect('index')
    else:
        formaPedido=PedidoForm()
        return render(request,'agregarPedido.html',{'formaPedido':formaPedido})

def editarPedido(request,id):
    pedido = get_object_or_404(Pedido,pk=id)
    if request.method == "POST":
        formaPedido = PedidoForm(request.POST,instance=pedido)
        if formaPedido.is_valid():
            formaPedido.save()
            return redirect('index')
    else:
        formaPedido = PedidoForm(instance=pedido)
        return render(request,'editarPedido.html',{'formaPedido':formaPedido})

def eliminarPedido(request,id):
    pedido = get_object_or_404(Pedido,pk=id)
    if pedido:
        pedido.delete()
    return redirect('index')

# Create your views here.

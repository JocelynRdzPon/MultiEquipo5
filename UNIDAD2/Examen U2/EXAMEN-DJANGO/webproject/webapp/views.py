from django.shortcuts import render, redirect, get_object_or_404
from gestorapp.models import Pedido, DetallePedido
from webapp.models import Cliente, Categoria, Producto
from webapp.forms import ClienteForm, CategoriaForm, ProductoForm


# Create your views here.
def index(req):
    pedido = Pedido.objects.order_by('id')
    detallePedido = DetallePedido.objects.order_by('id')
    return render(req,'index.html',{'pedido':pedido, 'detallePedido':detallePedido })

def indexClientes(req):
    noClientes =  Cliente.objects.count()
    clientes  =  Cliente.objects.order_by('id')
    
    return render(req,'indexClientes.html',{'noClientes': noClientes,'clientes': clientes })

def indexCategorias(req):
    noCategorias =  Categoria.objects.count()
    categorias  =  Categoria.objects.order_by('id')
    
    return render(req,'indexCategorias.html',{'noClientes': noCategorias,'clientes': categorias })

def indexProductos(req):
    noProductos =  Producto.objects.count()
    productos  =  Producto.objects.order_by('id')
    
    return render(req,'indexProductos.html',{'noProductos': noProductos,'productos': productos })

def indexDetallePedido(req):
    noDetalles =  DetallePedido.objects.count()
    detalles  =  DetallePedido.objects.order_by('id')
    return render(req,'indexDetalle.html',{'noDetalles': noDetalles,'detalles': detalles })

def indexPedido(req):
    noPedidos =  Pedido.objects.count()
    pedidos  =  Pedido.objects.order_by('id')
    
    return render(req,'indexPedidos.html',{'': noPedidos,'pedidos': pedidos })

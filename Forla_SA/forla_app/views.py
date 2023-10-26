from django.shortcuts import render
from .models import Producto, Cliente, Categoria, Pedido


# Create your views here.

def home(request):
    return render(request, "padre.html")


def producto(request):
    productos = Producto.objects.all()
    return render(request, "productos.html", {"productos": productos})

def nosotros(request):
    return render(request, "nosotros.html")

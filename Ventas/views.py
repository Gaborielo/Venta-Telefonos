from django.shortcuts import render, redirect, get_object_or_404
from .models import Pedido, Cliente, Telefono, Marca


def crear_pedido(request):
    if request.method == 'POST':
        Pedido.objects.create(
            cliente_id=request.POST['cliente'],
            total=request.POST['total'],
            estado=request.POST['estado']
        )
        return redirect('lista_telefonos')

    clientes = Cliente.objects.all()
    return render(request, 'ventas/crear_pedido.html', {
        'clientes': clientes
    })


def lista_telefonos(request):
    telefonos = Telefono.objects.all()
    return render(request, 'ventas/lista_telefonos.html', {
        'telefonos': telefonos
    })


def crear_telefono(request):
    if request.method == 'POST':
        Telefono.objects.create(
            marca_id=request.POST['marca'],
            modelo=request.POST['modelo'],
            precio=request.POST['precio'],
            stock=request.POST['stock'],
            descripcion=request.POST['descripcion']
        )
        return redirect('lista_telefonos')

    marcas = Marca.objects.all()
    return render(request, 'ventas/crear_telefono.html', {
        'marcas': marcas
    })


def editar_telefono(request, id):
    telefono = get_object_or_404(Telefono, id=id)

    if request.method == 'POST':
        telefono.modelo = request.POST['modelo']
        telefono.precio = request.POST['precio']
        telefono.stock = request.POST['stock']
        telefono.descripcion = request.POST['descripcion']
        telefono.save()
        return redirect('lista_telefonos')

    return render(request, 'ventas/editar_telefono.html', {
        'telefono': telefono
    })


def eliminar_telefono(request, id):
    telefono = get_object_or_404(Telefono, id=id)
    telefono.delete()
    return redirect('lista_telefonos')



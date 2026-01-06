from django.shortcuts import get_object_or_404, render, redirect
from .models import Cliente, Marca, Pedido, DetallePedido, Telefono
from django.db import transaction

def crear_pedido(request):
    if request.method == 'POST':
        cliente_id = request.POST.get('cliente')
        estado = request.POST.get('estado')

        telefonos_ids = request.POST.getlist('telefonos')
        cantidades = request.POST.getlist('cantidades')

        with transaction.atomic():
            pedido = Pedido.objects.create(
                cliente_id=cliente_id,
                total=0,
                estado=estado
            )

            total = 0

            for telefono_id, cantidad in zip(telefonos_ids, cantidades):
                telefono = Telefono.objects.get(id=telefono_id)
                cantidad = int(cantidad)

                subtotal = telefono.precio * cantidad
                total += subtotal

                DetallePedido.objects.create(
                    pedido=pedido,
                    telefono=telefono,
                    cantidad=cantidad,
                    precio_unitario=telefono.precio
                )

            pedido.total = total
            pedido.save()

        return redirect('lista_telefonos')

    clientes = Cliente.objects.all()
    telefonos = Telefono.objects.all()

    return render(request, 'crear_pedido.html', {
        'clientes': clientes,
        'telefonos': telefonos
    })


def lista_telefonos(request):
    telefonos = Telefono.objects.all()
    return render(request, 'lista_telefonos.html', {
        'telefonos': telefonos
    })


def crear_telefono(request):
    if request.method == 'POST':
        Telefono.objects.create(
            marca_id=request.POST.get('marca'),
            modelo=request.POST.get('modelo'),
            precio=request.POST.get('precio'),
            descripcion=request.POST.get('descripcion'),
            imagen=request.FILES.get('imagen')  # opcional
        )
        return redirect('lista_telefonos')

    marcas = Marca.objects.all()
    return render(request, 'crear_telefono.html', {
        'marcas': marcas
    })


def editar_telefono(request, id):
    telefono = get_object_or_404(Telefono, id=id)
    marcas = Marca.objects.all()

    if request.method == 'POST':
        telefono.marca_id = request.POST.get('marca')
        telefono.modelo = request.POST.get('modelo')
        telefono.precio = request.POST.get('precio')
        telefono.descripcion = request.POST.get('descripcion')

        # Imagen opcional
        if request.FILES.get('imagen'):
            telefono.imagen = request.FILES.get('imagen')

        telefono.save()
        return redirect('lista_telefonos')

    return render(request, 'editar_telefono.html', {
        'telefono': telefono,
        'marcas': marcas
    })


def eliminar_telefono(request, id):
    telefono = get_object_or_404(Telefono, id=id)

    if request.method == 'POST':
        telefono.delete()
        return redirect('lista_telefonos')

    return render(request, 'eliminar_telefono.html', {
        'telefono': telefono
    })


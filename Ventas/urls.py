from django.urls import path
from .views import (crear_pedido,lista_telefonos,crear_telefono,editar_telefono,eliminar_telefono
)

urlpatterns = [
    path('pedido/nuevo/', crear_pedido, name='crear_pedido'),

    path('telefonos/', lista_telefonos, name='lista_telefonos'),
    path('telefonos/nuevo/', crear_telefono, name='crear_telefono'),
    path('telefonos/editar/<int:id>/', editar_telefono, name='editar_telefono'),
    path('telefonos/eliminar/<int:id>/', eliminar_telefono, name='eliminar_telefono'),
]



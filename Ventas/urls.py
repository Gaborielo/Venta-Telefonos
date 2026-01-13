from django.urls import path
from .views import (crear_pedido,lista_telefonos,crear_telefono,editar_telefono,eliminar_telefono)
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', lista_telefonos, name='lista_telefonos'),
    path('pedido/nuevo/', crear_pedido, name='crear_pedido'),
    path('telefonos/', lista_telefonos, name='lista_telefonos'),
    path('telefonos/nuevo/', crear_telefono, name='crear_telefono'),
    path('telefonos/editar/<int:id>/', editar_telefono, name='editar_telefono'),
    path('telefonos/eliminar/<int:id>/', eliminar_telefono, name='eliminar_telefono'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]



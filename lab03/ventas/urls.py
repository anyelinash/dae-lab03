from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registrar/proveedor/', views.registrar_proveedor, name='registrar_proveedor'),
    path('visualizar/proveedores/', views.visualizar_proveedores, name='visualizar_proveedores'),
    path('registrar/cliente/', views.registrar_cliente, name='registrar_cliente'),
    path('visualizar/clientes/', views.visualizar_clientes, name='visualizar_clientes'),
    path('registrar/venta/', views.registrar_venta, name='registrar_venta'),
    path('registrar/producto_vendido/', views.registrar_producto_vendido, name='registrar_producto_vendido'), 
    path('registrar/producto/', views.registrar_producto, name='registrar_producto'),  # Nueva URL para registrar productos
    path('visualizar/productos/', views.visualizar_productos, name='visualizar_productos'),  # Nueva URL para visualizar productos
    path('ventas/visualizar/', views.visualizar_ventas, name='visualizar_ventas'),
]

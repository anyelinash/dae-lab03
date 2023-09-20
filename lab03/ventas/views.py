from django.shortcuts import render, redirect
from .models import Proveedor, Cliente, Venta, Producto, ProductoVendido, CategoriaProducto
from decimal import Decimal


def index(request):
    return render(request, 'ventas/index.html')

def registrar_proveedor(request):
    if request.method == 'POST':
        # Maneja el proceso de registro del proveedor aquí
        codigo = request.POST['codigo']
        nombre = request.POST['nombre']
        direccion = request.POST['direccion']
        telefono = request.POST['telefono']
        pagina_web = request.POST['pagina_web']
        
        # Crea un objeto Proveedor y guárdalo en la base de datos
        proveedor = Proveedor(
            codigo=codigo,
            nombre=nombre,
            direccion=direccion,
            telefono=telefono,
            pagina_web=pagina_web
        )
        proveedor.save()
        
        return redirect('visualizar_proveedores')  # Redirige a la vista de visualización
    return render(request, 'ventas/registro_proveedor.html')

def visualizar_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'ventas/visualizar_proveedores.html', {'proveedores': proveedores})

def registrar_cliente(request):
    if request.method == 'POST':
        # Maneja el proceso de registro del cliente aquí
        codigo = request.POST['codigo']
        nombre = request.POST['nombre']
        direccion_calle = request.POST['direccion_calle']
        direccion_numero = request.POST['direccion_numero']
        direccion_comuna = request.POST['direccion_comuna']
        direccion_ciudad = request.POST['direccion_ciudad']
        
        # Crea un objeto Cliente y guárdalo en la base de datos
        cliente = Cliente(
            codigo=codigo,
            nombre=nombre,
            direccion_calle=direccion_calle,
            direccion_numero=direccion_numero,
            direccion_comuna=direccion_comuna,
            direccion_ciudad=direccion_ciudad
        )
        cliente.save()
        
        return redirect('visualizar_clientes')  # Redirige a la vista de visualización
    return render(request, 'ventas/registro_cliente.html')

def visualizar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'ventas/visualizar_clientes.html', {'clientes': clientes})

def registrar_venta(request):
    if request.method == 'POST':
        # Obtén los datos del formulario
        numero_factura = request.POST['numero_factura']
        fecha = request.POST['fecha']
        cliente_id = request.POST['cliente']
        descuento = Decimal(request.POST['descuento'])  # Convierte el descuento a Decimal

        # Crea un objeto Venta sin el campo monto_final por ahora
        venta = Venta(
            numero_factura=numero_factura,
            fecha=fecha,
            cliente_id=cliente_id,
            descuento=descuento
        )
        venta.save()
        productos_vendidos = request.POST.getlist('productos_vendidos')
        monto_final = Decimal('0.00')  # Inicializa el monto final en 0.00

        for producto_id in productos_vendidos:
            # Aquí debes agregar la lógica para procesar los productos vendidos
            # Por ejemplo, obtener el producto por su ID y calcular el monto total
            producto = Producto.objects.get(id=producto_id)
            precio_venta = producto.precio_actual
            cantidad_vendida = 1  # Puedes ajustar esto según tus necesidades
            monto_total = precio_venta * cantidad_vendida

            # Crear un objeto ProductoVendido y asociarlo con la venta
            producto_vendido = ProductoVendido(
                producto=producto,
                precio_venta=precio_venta,
                cantidad_vendida=cantidad_vendida,
                monto_total=monto_total
            )
            producto_vendido.save()
            venta.productos_vendidos.add(producto_vendido)
            monto_final += monto_total

        # Aplica el descuento a la venta (si hay un descuento válido)
        if descuento > Decimal('0.00'):
            monto_final -= (monto_final * (descuento / Decimal('100.00')))  # Resta el descuento al monto final

        # Asigna el valor calculado a monto_final
        venta.monto_final = monto_final
        venta.save()

        return redirect('visualizar_ventas')  # Redirige a la vista de visualización de ventas

    # Lógica para cargar los datos necesarios para el formulario (clientes y productos)
    clientes = Cliente.objects.all()
    productos = Producto.objects.all()
    return render(request, 'ventas/registro_venta.html', {'clientes': clientes, 'productos': productos})

def visualizar_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'ventas/visualizar_ventas.html', {'ventas': ventas})

def registrar_producto_vendido(request):
    if request.method == 'POST':
        # Maneja el proceso de registro del producto vendido aquí
        producto_id = request.POST['producto']
        precio_venta = request.POST['precio_venta']
        cantidad_vendida = request.POST['cantidad_vendida']

        # Crea un objeto ProductoVendido y guárdalo en la base de datos
        producto_vendido = ProductoVendido(
            producto_id=producto_id,
            precio_venta=precio_venta,
            cantidad_vendida=cantidad_vendida
        )
        producto_vendido.save()

        return redirect('registrar_producto_vendido')  # Redirige a la vista de registro nuevamente

    productos = Producto.objects.all()
    return render(request, 'ventas/registro_producto_vendido.html', {'productos': productos})
    
def registrar_producto(request):
    if request.method == 'POST':
        # Maneja el proceso de registro del producto aquí
        identificador = request.POST['identificador']
        nombre = request.POST['nombre']
        precio_actual = request.POST['precio_actual']
        stock = request.POST['stock']
        proveedor_id = request.POST['proveedor']
        categoria_id = request.POST['categoria']

        # Crea un objeto Producto y guárdalo en la base de datos
        producto = Producto(
            identificador=identificador,
            nombre=nombre,
            precio_actual=precio_actual,
            stock=stock,
            proveedor_id=proveedor_id,
            categoria_id=categoria_id
        )
        producto.save()

        return redirect('visualizar_productos')
    
    # Si la solicitud no es POST, obtén todos los proveedores antes de renderizar el formulario
    proveedores = Proveedor.objects.all()
    categorias = CategoriaProducto.objects.all()

    return render(request, 'ventas/registro_producto.html', {'proveedores': proveedores, 'categorias': categorias})

def visualizar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'ventas/visualizar_productos.html', {'productos': productos})
from django.db import models
# Create your models here.
class Proveedor(models.Model):
    codigo = models.CharField(unique=True, max_length=20)
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()
    telefono = models.CharField(max_length=20)
    pagina_web = models.URLField()

class Cliente(models.Model):
    codigo = models.CharField(unique=True, max_length=20)
    nombre = models.CharField(max_length=100)
    direccion_calle = models.CharField(max_length=100)
    direccion_numero = models.CharField(max_length=10)
    direccion_comuna = models.CharField(max_length=50)
    direccion_ciudad = models.CharField(max_length=50)
    telefonos_contacto = models.ManyToManyField('TelefonoContacto', blank=True)

class TelefonoContacto(models.Model):
    numero = models.CharField(max_length=20)

class CategoriaProducto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

class Producto(models.Model):
    identificador = models.CharField(unique=True, max_length=20)
    nombre = models.CharField(max_length=100)
    precio_actual = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE)

class Venta(models.Model):
    numero_factura = models.CharField(unique=True, max_length=20)
    fecha = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    descuento = models.DecimalField(max_digits=10, decimal_places=2)
    monto_final = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    productos_vendidos = models.ManyToManyField('ProductoVendido')

class ProductoVendido(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_vendida = models.PositiveIntegerField()
    monto_total = models.DecimalField(max_digits=10, decimal_places=2, null=True)
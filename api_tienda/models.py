from django.db import models

# Modelo Categoría.
class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=500)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre_categoria


# Modelo Producto
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=255)
    cantidad = models.IntegerField(default=0)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    estado = models.BooleanField(default=True)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    
    def __str__(self):
        return self.nombre


# Modelo Cliente
class Cliente(models.Model):
    cedula = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255, blank=True)
    telefono = models.CharField(max_length=10)
    email = models.EmailField(max_length=255, unique=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.cedula}  -  {self.nombre} {self.apellido}'
    

# Modelo Pedidos
class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pedidos')
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    detalle = models.TextField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.detalle}  -  ${self.precio}'


# Modelo DetallePedido.
class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='detalle_pedidos')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='detalle_productos')
    cantidad = models.IntegerField(default=0)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f'{self.producto} - {self.cantidad}'


# Modelo de Pago.
class Pago(models.Model):
    METODOS_PAGO = [
        ('TC', 'Tarjeta de Crédito'),
        ('PP', 'PayPal'),
        ('TB', 'Transferencia Bancaria'),
    ]
    ESTADOS_PAGO = [
        ('PEN', 'Pendiente'),
        ('COM', 'Completado'),
        ('RECH', 'Rechazado'),
    ]

    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='pagos')
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=3, choices=METODOS_PAGO, default='TC')
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=4, choices=ESTADOS_PAGO, default='PEN')

    def __str__(self):
        return f'{self.pedido}'


# Modelo Inventario
class Inventario(models.Model):
    producto = models.OneToOneField(Producto, on_delete=models.CASCADE, related_name='inventario')
    cantidad_disponible = models.IntegerField(default=0)
    ubicacion = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.producto.nombre} - {self.cantidad_disponible} unidades'
    
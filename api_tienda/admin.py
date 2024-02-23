from django.contrib import admin
from api_tienda.models import (
    Producto, 
    Cliente, 
    Categoria, 
    Pedido, 
    DetallePedido, 
    Pago, 
    Inventario)

# Register your models here.
admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Categoria)
admin.site.register(Pedido)
admin.site.register(DetallePedido)
admin.site.register(Pago)
admin.site.register(Inventario)


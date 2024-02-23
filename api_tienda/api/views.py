from rest_framework import viewsets
from api_tienda.models import (
    Producto, 
    Cliente, 
    Categoria, 
    Pedido, 
    DetallePedido, 
    Pago, 
    Inventario
)
from api_tienda.api.serializers import (
    ProductoSerializer, 
    ClienteSerializer, 
    CategoriaSerializer, 
    PedidoSerializer, 
    DetallePedidoSerializer, 
    PagoSerializer, 
    InventarioSerializer
)
from api_tienda.api.permission import IsAdminOrReadOnlyAuthenticated


# VIEWS APIS.
class ProductoView(viewsets.ModelViewSet):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all()
    #permission_classes = [IsAdminOrReadOnlyAuthenticated]


class ClienteView(viewsets.ModelViewSet):
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all()


class CategoriaView(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class PedidoView(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer


class DetallePedidoView(viewsets.ModelViewSet):
    queryset = DetallePedido.objects.all()
    serializer_class = DetallePedidoSerializer


class PagoView(viewsets.ModelViewSet):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer


class InventarioView(viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer
    

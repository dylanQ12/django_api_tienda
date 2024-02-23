from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api_tienda.api.views import (
    ProductoView,
    ClienteView,
    CategoriaView,
    PedidoView,
    DetallePedidoView,
    PagoView,
    InventarioView,
)

router = DefaultRouter()
router.register(r'categorias', CategoriaView, basename='categoria')
router.register(r'productos', ProductoView, basename='producto')
router.register(r'clientes', ClienteView, basename='cliente')
router.register(r'pedidos', PedidoView, basename='pedido')
router.register(r'detalle-pedidos', DetallePedidoView, basename='detalle-pedido')
router.register(r'pagos', PagoView, basename='pago')
router.register(r'inventarios', InventarioView, basename='inventario')

urlpatterns = [
    # RUTA DE LA API.
    path('api/', include(router.urls)),
]


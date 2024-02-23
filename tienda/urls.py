from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tienda/', include('api_tienda.api.urls')),
    path('account/', include('usuarios.api.urls')),
]

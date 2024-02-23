from rest_framework import permissions

from rest_framework import permissions

class IsAdminOrReadOnlyAuthenticated(permissions.BasePermission):
    """
    Permiso personalizado que permite a los usuarios autenticados realizar operaciones de lectura,
    permite a los administradores realizar operaciones CRUD, y restringe a los usuarios anónimos
    a solo operaciones de lectura.
    """

    def has_permission(self, request, view):
        # Permite solicitudes de lectura para cualquier usuario
        if request.method in permissions.SAFE_METHODS:
            return True

        # Permite todas las operaciones CRUD solo si el usuario está autenticado y es administrador
        return request.user and request.user.is_authenticated and request.user.is_staff
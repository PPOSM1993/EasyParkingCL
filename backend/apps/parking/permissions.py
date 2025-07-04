from rest_framework import permissions

class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Permite modificar solo al dueño o al admin.
    """

    def has_object_permission(self, request, view, obj):
        # Lectura permitida para cualquier usuario autenticado
        if request.method in permissions.SAFE_METHODS:
            return True

        # Modificación permitida solo para dueño o admin
        return obj.owner == request.user or request.user.is_staff

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Permiso que permite solo al owner editar o borrar, pero cualquiera puede ver (GET, HEAD, OPTIONS).
    """

    def has_object_permission(self, request, view, obj):
        # Métodos seguros permitidos para cualquiera
        if request.method in permissions.SAFE_METHODS:
            return True

        # Solo el owner puede editar o borrar
        return obj.owner == request.user
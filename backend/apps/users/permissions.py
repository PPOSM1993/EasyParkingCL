from rest_framework import permissions

class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Permite a los usuarios ver/editar su propio perfil.
    Solo los administradores pueden ver/editar a cualquier usuario.
    """

    def has_object_permission(self, request, view, obj):
        # Si el método es "safe" (GET, HEAD, OPTIONS), permite ver.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Permite modificar si es el propio usuario o si es admin
        return obj == request.user or (request.user.is_authenticated and request.user.role == 'admin')

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

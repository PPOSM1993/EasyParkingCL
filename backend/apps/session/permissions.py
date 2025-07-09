from rest_framework import permissions

class IsOwnerOrAdminSession(permissions.BasePermission):
    """
    Permite el acceso solo al dueño de la sesión o a usuarios con rol 'admin'.
    """

    def has_object_permission(self, request, view, obj):
        # Admin puede acceder a todo
        if hasattr(request.user, 'role') and request.user.role == 'admin':
            return True
        # El dueño puede acceder a su propia sesión
        return obj.user == request.user

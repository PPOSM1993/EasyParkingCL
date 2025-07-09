from rest_framework import permissions

class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Permite acceso solo al dueño de la notificación o a usuarios admin/staff.
    """

    def has_object_permission(self, request, view, obj):
        user = request.user
        return (
            obj.user == user or
            user.is_staff or
            getattr(user, 'role', None) == 'admin'
        )

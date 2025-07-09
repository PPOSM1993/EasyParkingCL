"""from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from django.utils.translation import gettext_lazy as _

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    pass"""
    # Campos que se muestran en la lista de usuarios en el admin
"""    list_display = (
        'username', 'email', 'first_name', 'last_name',
        'rut', 'phone_number', 'role', 'is_active', 'is_staff', 'is_verified'
    )
    list_filter = ('role', 'is_verified', 'is_staff', 'is_superuser', 'is_active')

    # Campos para la vista de detalle (al editar)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Información personal'), {
            'fields': (
                'first_name', 'last_name', 'email', 'rut', 'phone_number',
                'address', 'date_of_birth', 'profile_image', 'language'
            )
        }),
        (_('Permisos'), {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions', 'role', 'is_verified'
            )
        }),
        (_('Preferencias y otros'), {
            'fields': ('preferences', 'notifications_enabled')
        }),
        (_('Fechas importantes'), {'fields': ('last_login', 'date_joined')}),
    )

    # Campos para la vista de creación de usuarios en el admin
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username', 'email', 'password1', 'password2',
                'rut', 'role', 'is_staff', 'is_active'
            ),
        }),
    )

    search_fields = ('username', 'email', 'rut', 'first_name', 'last_name')
    ordering = ('-date_joined',)
"""
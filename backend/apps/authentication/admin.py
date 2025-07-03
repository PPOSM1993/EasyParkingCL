from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'rut', 'is_active', 'is_staff', 'date_joined', 'phone']
    list_filter = ['is_active', 'is_staff', 'accepted_terms']
    search_fields = ['username', 'email', 'first_name', 'last_name', 'rut', 'phone']
    ordering = ['-date_joined']
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Información personal', {'fields': ('first_name', 'last_name', 'rut', 'phone', 'birth_date')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Términos', {'fields': ('accepted_terms',)}),
        ('Fechas importantes', {'fields': ('last_login', 'date_joined')}),
    )
    readonly_fields = ['date_joined', 'last_login']
from django.contrib import admin
from .models import RouteRequest, RecommendedZone


@admin.register(RouteRequest)
class RouteRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__email',)


@admin.register(RecommendedZone)
class RecommendedZoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'zone', 'route_request', 'is_primary', 'created_at')
    list_filter = ('is_primary', 'created_at')
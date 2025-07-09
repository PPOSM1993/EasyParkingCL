"""from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import PermissionDenied

from .models import User
from .serializers import UserSerializer
from .permissions import IsOwnerOrAdmin
from .filters import UserFilter

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrAdmin]
    filter_backends = [DjangoFilterBackend]
    filterset_class = UserFilter

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return User.objects.all().order_by('-date_joined')
        return User.objects.filter(id=user.id)

    def get_object(self):
        obj = super().get_object()
        if self.request.user != obj and self.request.user.role != 'admin':
            raise PermissionDenied("No tienes permiso para acceder a este perfil.")
        return obj

    @action(detail=False, methods=['get'])
    def me(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)
"""
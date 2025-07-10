from rest_framework import viewsets, permissions, filters
from .models import Payment
from .serializers import PaymentSerializer
from .permissions import IsOwnerOrAdmin
from django_filters.rest_framework import DjangoFilterBackend
from .filters import PaymentFilter

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filterset_class = PaymentFilter
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['status', 'method', 'currency']
    search_fields = ['user__username', 'transaction_id', 'description']
    ordering_fields = ['created_at', 'amount', 'paid_at']
    ordering = ['-created_at']

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.role == 'admin':
            return Payment.objects.all()
        return Payment.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

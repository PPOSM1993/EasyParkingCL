from django.urls import path
from .views import RegisterView, CustomLoginView, LogoutView, ConfirmEmailView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),  # <-- exacto
    path('logout/', LogoutView.as_view(), name='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('confirm-email/<uidb64>/<token>/', ConfirmEmailView.as_view(), name='confirm-email'),
]


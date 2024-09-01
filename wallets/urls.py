from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import WalletViewSet, TransactionViewSet


app_name = 'wallets'

urlpatterns = [
    # ограничиваем возможности ModelViewSet в целях безопасности
    path('wallet/', WalletViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('wallet/<int:pk>/', WalletViewSet.as_view({'get': 'retrieve'})),
    path('transactions/', TransactionViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('transactions/<int:pk>/', TransactionViewSet.as_view({'get': 'retrieve'})),
]

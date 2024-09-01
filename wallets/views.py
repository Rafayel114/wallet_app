from django_filters.rest_framework import DjangoFilterBackend
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from .models import Wallet, Transaction
from .serializers import WalletSerializer, TransactionSerializer
from .filters import WalletFilter, TransactionFilter
from .decorators import timeout_decorator
import time


class WalletViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = WalletFilter
    ordering_fields = '__all__'
    ordering = ['label']

    @timeout_decorator(4)
    def get_queryset(self):
        # Возвращаем только кошелек, принадлежащий текущему пользователю
        user = self.request.user
        return Wallet.objects.filter(user=user)


class TransactionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TransactionFilter
    ordering_fields = '__all__'
    ordering = ['txid']

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except ValidationError as e:
            return JsonResponse({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
    @timeout_decorator(4)
    def get_queryset(self):
        # Возвращаем только транзавкции, принадлежащие текущему пользователю
        user = self.request.user
        return Transaction.objects.filter(wallet__user=user)

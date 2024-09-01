from .models import Wallet, Transaction
import django_filters as filters


class WalletFilter(filters.FilterSet):
    balance = filters.NumberFilter(field_name='balance', lookup_expr='exact')
    min_balance = filters.NumberFilter(field_name="balance", lookup_expr='gte')
    max_balance = filters.NumberFilter(field_name="balance", lookup_expr='lte')

    class Meta:
        model = Wallet
        fields = ['min_balance', 'max_balance']


class TransactionFilter(filters.FilterSet):
    amount = filters.NumberFilter(field_name='amount', lookup_expr='exact')
    min_amount = filters.NumberFilter(field_name="amount", lookup_expr='gte')
    max_amount = filters.NumberFilter(field_name="amount", lookup_expr='lte')

    class Meta:
        model = Transaction
        fields = ['min_amount', 'max_amount']
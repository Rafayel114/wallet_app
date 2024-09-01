import pytest
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from rest_framework.test import APIClient
from .models import Wallet, Transaction


class WalletAPITestCase(TestCase):

    def setUp(self):
        self.client = APIClient()

        self.wallet = Wallet.objects.create(label="Test Wallet")

        self.user = get_user_model().objects.create_user(
            email='testuser@example.com',
            password='password123',
            wallet=self.wallet
        )
        response = self.client.post('/api/auth/token/', {
            'email': 'testuser@example.com',
            'password': 'password123'
        })
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_wallet_creation(self):
        response = self.client.post('/api/wallets/wallet/', {'label': 'New Wallet'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Wallet.objects.count(), 2)


class TestTransactionSaveMethod(TestCase):

    def test_add_amount_to_balance(self):
        wallet = Wallet.objects.create(balance=100)
        transaction = Transaction(wallet=wallet, amount=50, txid="test1111111")
        transaction.save()
        # Проверяем, что баланс увеличился на 50
        wallet.refresh_from_db()
        self.assertEqual(wallet.balance, 150)

        transaction = Transaction(wallet=wallet, amount=-40, txid="test222222")
        transaction.save()
        # Проверяем, что баланс уменьшился на 40
        wallet.refresh_from_db()
        self.assertEqual(wallet.balance, 110)

    def test_cannot_make_balance_negative(self):
        wallet = Wallet.objects.create(balance=100)
        transaction = Transaction(wallet=wallet, amount=-150, txid="test333333")
        with self.assertRaises(ValidationError):
            transaction.save()
        # Проверяем, что баланс кошелька не изменился
        wallet.refresh_from_db()
        self.assertEqual(wallet.balance, 100)
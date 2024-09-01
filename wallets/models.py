from django.db import models, transaction
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from .methods import generate_unique_label


class Wallet(models.Model):
    label = models.CharField(
        max_length=255, 
        unique=True,
        db_index=True, 
        default=generate_unique_label
    )
    balance = models.DecimalField(max_digits=30, decimal_places=18, default=0)
    
    def __str__(self):
        return self.label

    def save(self, *args, **kwargs):
        if self.balance < 0:
            raise ValidationError("Баланс не может быть отрицательным")
        super().save(*args, **kwargs)


class Transaction(models.Model):
    wallet = models.ForeignKey(
        Wallet, 
        related_name='transactions', 
        on_delete=models.DO_NOTHING
    )
    txid = models.CharField(
        max_length=255, 
        unique=True,
        db_index=True
    )
    amount = models.DecimalField(max_digits=30, decimal_places=18)

    def save(self, *args, **kwargs):
        # Откроем атомарную транзакцию
        with transaction.atomic():
            # Пересчитываем баланс
            self.wallet.balance += self.amount
            if self.wallet.balance < 0:
                raise ValidationError("Баланс кошелька не может стать отрицательным")
            # Сохраняем кошелек и транзакцию
            self.wallet.save()
            super().save(*args, **kwargs)

    def __str__(self):
        return f"Transaction {self.txid} for Wallet {self.wallet.label}, amount {self.amount}"
    
# Generated by Django 4.2.15 on 2024-08-31 14:10

from django.db import migrations, models
import django.db.models.deletion
import wallets.methods


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(db_index=True, default=wallets.methods.generate_unique_label, max_length=255, unique=True)),
                ('balance', models.DecimalField(decimal_places=18, default=0, max_digits=30)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txid', models.CharField(db_index=True, max_length=255, unique=True)),
                ('amount', models.DecimalField(decimal_places=18, max_digits=30)),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='transactions', to='wallets.wallet')),
            ],
        ),
    ]

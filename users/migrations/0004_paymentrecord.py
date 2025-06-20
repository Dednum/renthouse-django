# Generated by Django 5.2 on 2025-06-14 17:11

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_customuser_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentRecord',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(help_text='Full name of the person making the payment.', max_length=100)),
                ('email', models.EmailField(help_text='Email address of the person making the payment.', max_length=100)),
                ('phone_number', models.CharField(blank=True, help_text='Phone number of the person making the payment.', max_length=20, null=True)),
                ('amount', models.DecimalField(decimal_places=2, help_text='Amount paid.', max_digits=10)),
                ('payment_date', models.DateTimeField(default=django.utils.timezone.now, help_text='Date and time the payment was recorded.')),
                ('transaction_id', models.CharField(blank=True, help_text='Unique transaction ID from payment gateway.', max_length=255, null=True, unique=True)),
                ('payment_method', models.CharField(blank=True, help_text='e.g., Credit Card, Bank Transfer, Online Wallet.', max_length=50, null=True)),
                ('booking', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='payment_records', to='users.booking')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='payment_records', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Payment Records',
                'ordering': ['-payment_date'],
            },
        ),
    ]

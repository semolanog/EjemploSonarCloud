# Generated by Django 5.1.3 on 2024-11-23 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('active', models.BooleanField(default=True, help_text='Indicates whether the payment method is currently active.')),
                ('details', models.CharField(help_text='Secure details for the payment method, such as a token or card number.', max_length=255)),
                ('expiration_date', models.DateField(help_text='The expiration date of the payment method.')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('bank_transfer', 'Bank Transfer'), ('credit_card', 'Credit Card'), ('cryptocurrency', 'Cryptocurrency'), ('debit_card', 'Debit Card'), ('paypal', 'PayPal')], help_text='The type of the payment method.', max_length=14)),
            ],
            options={
                'verbose_name': 'PaymentMethod',
                'verbose_name_plural': 'PaymentMethods',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('admin', models.BooleanField(default=False, help_text='Indicates whether the user has admin permissions.')),
                ('email', models.EmailField(help_text="The user's email address.", max_length=254, unique=True)),
                ('favorite_genre_ids', models.TextField(blank=True, help_text="The ids for the user's favorite genres; may be null if no genres are defined.", null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(help_text="The user's full name.", max_length=255)),
                ('password', models.CharField(help_text="The user's password.", max_length=128)),
                ('payment_method_ids', models.ManyToManyField(blank=True, help_text='The ids of the payment methods related to the user.', to='users.paymentmethod')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
    ]

# Generated by Django 5.2.1 on 2025-06-24 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_orders', '0002_alter_telegramorder_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=50)),
                ('language', models.CharField(choices=[('ru', 'Русский'), ('uz', 'O‘zbekcha')], max_length=2)),
                ('service', models.CharField(max_length=100)),
                ('subservice', models.CharField(max_length=100)),
                ('tariff', models.CharField(choices=[('standard', 'Стандарт'), ('premium', 'Премиум')], max_length=20)),
                ('price', models.CharField(default='Договорная', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='TelegramOrder',
        ),
    ]

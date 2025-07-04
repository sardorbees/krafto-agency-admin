# Generated by Django 5.2.1 on 2025-06-05 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категория'},
        ),
        migrations.AlterModelOptions(
            name='favoriteproduct',
            options={'verbose_name': 'Добавить корзину', 'verbose_name_plural': 'Добавить корзину'},
        ),
        migrations.AlterModelOptions(
            name='feedback',
            options={'verbose_name': 'Добавить изб', 'verbose_name_plural': 'Добавить изб'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товар'},
        ),
        migrations.AlterModelOptions(
            name='productimage',
            options={'verbose_name': 'Товар-фото', 'verbose_name_plural': 'Товар-фото'},
        ),
        migrations.AlterModelOptions(
            name='productsize',
            options={'verbose_name': 'Категория размера', 'verbose_name_plural': 'Категория размера'},
        ),
        migrations.AlterModelOptions(
            name='producttags',
            options={'verbose_name': 'Категория тега', 'verbose_name_plural': 'Категория тега'},
        ),
    ]

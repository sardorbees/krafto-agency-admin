# Generated by Django 5.2.1 on 2025-06-25 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('language', '0004_languagepreference_delete_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='languagepreference',
            name='language',
            field=models.CharField(choices=[('ru', 'Русский'), ('uz', "O'zbekcha")], max_length=10),
        ),
        migrations.AlterField(
            model_name='languagepreference',
            name='session_id',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]

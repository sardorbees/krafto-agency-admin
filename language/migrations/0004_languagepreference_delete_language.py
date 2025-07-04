# Generated by Django 5.2.1 on 2025-06-25 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('language', '0003_alter_language_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='LanguagePreference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_id', models.CharField(max_length=255, unique=True)),
                ('language', models.CharField(choices=[('ru', 'Русский'), ('uz', 'O‘zbekcha')], max_length=2)),
            ],
        ),
        migrations.DeleteModel(
            name='Language',
        ),
    ]

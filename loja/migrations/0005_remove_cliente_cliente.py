# Generated by Django 5.1.4 on 2025-03-12 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0004_rename_usuario_cliente_cliente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='cliente',
        ),
    ]

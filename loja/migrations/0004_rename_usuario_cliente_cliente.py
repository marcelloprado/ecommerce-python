# Generated by Django 5.1.4 on 2025-03-12 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0003_rename_cliente_cliente_usuario_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='usuario',
            new_name='cliente',
        ),
    ]

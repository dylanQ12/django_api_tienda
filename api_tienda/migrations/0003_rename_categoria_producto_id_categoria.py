# Generated by Django 4.2 on 2024-02-23 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_tienda', '0002_alter_categoria_descripcion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='categoria',
            new_name='id_categoria',
        ),
    ]
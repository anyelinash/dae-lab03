# Generated by Django 4.2.5 on 2023-09-20 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0002_alter_venta_monto_final'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productovendido',
            name='monto_total',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]

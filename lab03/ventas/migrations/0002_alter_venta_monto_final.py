# Generated by Django 4.2.5 on 2023-09-20 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='monto_final',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]

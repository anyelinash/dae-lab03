# Generated by Django 4.2.5 on 2023-09-13 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encuesta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pregunta',
            name='pregunta_texto',
            field=models.CharField(max_length=20),
        ),
    ]

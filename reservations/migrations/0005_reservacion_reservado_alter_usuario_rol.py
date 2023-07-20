# Generated by Django 4.2.2 on 2023-07-18 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0004_rename_cantidad_personad_reservacion_cantidad_personas'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservacion',
            name='reservado',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='rol',
            field=models.CharField(default='usuario', max_length=20),
        ),
    ]
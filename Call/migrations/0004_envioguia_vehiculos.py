# Generated by Django 4.0.2 on 2022-04-11 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Vehiculos', '0002_remove_tipovehiculo_descripcion_tipovehiculo_created_and_more'),
        ('Call', '0003_envioguia'),
    ]

    operations = [
        migrations.AddField(
            model_name='envioguia',
            name='vehiculos',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vehiculos', to='Vehiculos.vehiculo'),
        ),
    ]

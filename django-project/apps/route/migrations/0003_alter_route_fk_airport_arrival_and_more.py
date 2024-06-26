# Generated by Django 5.0.6 on 2024-06-05 00:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airport', '0001_initial'),
        ('route', '0002_alter_route_fk_airport_arrival_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='fk_airport_arrival',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrival_routes', to='airport.airport'),
        ),
        migrations.AlterField(
            model_name='route',
            name='fk_airport_departure',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departure_routes', to='airport.airport'),
        ),
    ]

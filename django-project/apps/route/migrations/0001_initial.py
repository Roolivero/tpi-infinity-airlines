# Generated by Django 5.0.6 on 2024-05-19 01:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('airport', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fk_airport_arrival', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrival_routes', to='airport.airport')),
                ('fk_airport_departure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departure_routes', to='airport.airport')),
            ],
        ),
    ]

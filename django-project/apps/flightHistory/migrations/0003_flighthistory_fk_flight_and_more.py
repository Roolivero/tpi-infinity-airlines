# Generated by Django 5.0.6 on 2024-06-08 01:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0003_remove_flight_fk_flight_history_and_more'),
        ('flightHistory', '0002_flighthistory_sold_ticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='flighthistory',
            name='fk_flight',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='flight.flight'),
        ),
        migrations.AlterUniqueTogether(
            name='flighthistory',
            unique_together={('date', 'fk_flight')},
        ),
    ]

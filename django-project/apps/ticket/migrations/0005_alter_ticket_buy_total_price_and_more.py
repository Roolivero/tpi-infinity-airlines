# Generated by Django 5.0.6 on 2024-06-12 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0004_ticket_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='buy_total_price',
            field=models.FloatField(unique=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='seat_location',
            field=models.CharField(),
        ),
    ]

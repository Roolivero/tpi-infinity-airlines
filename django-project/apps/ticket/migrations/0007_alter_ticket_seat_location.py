# Generated by Django 5.0.6 on 2024-07-02 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0006_alter_ticket_buy_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='seat_location',
            field=models.CharField(max_length=4),
        ),
    ]
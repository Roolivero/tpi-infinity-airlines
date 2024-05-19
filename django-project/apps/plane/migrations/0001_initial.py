# Generated by Django 5.0.6 on 2024-05-19 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plane',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plane_model', models.CharField(max_length=50)),
                ('size', models.CharField(choices=[('chico', 'chico'), ('mediano', 'mediano'), ('grande', 'grande')], default='mediano', max_length=7)),
            ],
        ),
    ]
# Generated by Django 4.2.13 on 2024-06-03 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('AQ', 'Air Quality'), ('TM', 'Temperature'), ('PR', 'Pressure'), ('WS', 'Wind Speed'), ('WD', 'Wind Direction'), ('NO', 'Noise'), ('LT', 'Light'), ('UV', 'UV Index')], max_length=10)),
                ('installation_dat', models.DateField()),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('temperature', models.FloatField()),
                ('humidity', models.FloatField()),
                ('wind_speed', models.FloatField()),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.sensors')),
            ],
        ),
        migrations.CreateModel(
            name='Alerts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.sensors')),
            ],
        ),
    ]

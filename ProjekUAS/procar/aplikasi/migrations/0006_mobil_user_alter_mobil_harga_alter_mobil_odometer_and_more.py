# Generated by Django 5.0.6 on 2024-06-07 17:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplikasi', '0005_alter_mobil_kapasitas_mesin'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='mobil',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='mobil',
            name='harga',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='mobil',
            name='odometer',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='mobil',
            name='tahun',
            field=models.IntegerField(),
        ),
    ]

# Generated by Django 5.0.6 on 2024-06-10 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplikasi', '0007_alter_mobil_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobil',
            name='Penggerakroda',
            field=models.CharField(choices=[('0', '4x4'), ('1', '2x4')], default='2x4', max_length=3),
        ),
        migrations.AlterField(
            model_name='mobil',
            name='bahanbakar',
            field=models.CharField(choices=[('0', 'SOLAR'), ('1', 'BENSIN')], default='BENSIN', max_length=10),
        ),
        migrations.AlterField(
            model_name='mobil',
            name='kapasitas_mesin',
            field=models.CharField(choices=[('1000', '1000 CC'), ('1200', '1200 CC'), ('1300', '1300 CC'), ('1400', '1400 CC'), ('1500', '1500 CC'), ('1600', '1600 CC'), ('1800', '1800 CC'), ('2000', '2000 CC'), ('2200', '2200 CC'), ('2400', '2400 CC'), ('2500', '2500 CC'), ('2600', '2600 CC'), ('2800', '2800 CC'), ('3000', '3000 CC')], max_length=7),
        ),
        migrations.AlterField(
            model_name='mobil',
            name='kelayakan',
            field=models.CharField(choices=[('1', 'LAYAK'), ('0', 'TIDAK LAYAK')], default='TIDAK LAYAK', max_length=11),
        ),
        migrations.AlterField(
            model_name='mobil',
            name='transmisi',
            field=models.CharField(choices=[('0', 'AUTOMATIC'), ('1', 'MANUAL')], default='MANUAL', max_length=10),
        ),
    ]

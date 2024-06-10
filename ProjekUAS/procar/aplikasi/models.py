from django.db import models
from django.contrib.auth.models import User


class Merek(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Jenis(models.Model):
    name = models.CharField(max_length=50)
    merek = models.ForeignKey(Merek, on_delete=models.CASCADE, related_name='jenis')

    def __str__(self):
        return self.name

class Mobil(models.Model):
    
    PENGGERAK_RODA_CHOICES = (
        ('0', '4x4'),
        ('1', '2x4'),
    )

    KAPASITAS_MESIN_CHOICES = (
        ('1000', '1000 CC'),
        ('1200', '1200 CC'),
        ('1300', '1300 CC'),
        ('1400', '1400 CC'),
        ('1500', '1500 CC'),
        ('1600', '1600 CC'),
        ('1800', '1800 CC'),
        ('2000', '2000 CC'),
        ('2200', '2200 CC'),
        ('2400', '2400 CC'),
        ('2500', '2500 CC'),
        ('2600', '2600 CC'),
        ('2800', '2800 CC'),
        ('3000', '3000 CC'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    merek = models.ForeignKey(Merek, on_delete=models.CASCADE)
    jenis = models.ForeignKey(Jenis, on_delete=models.CASCADE)
    Penggerakroda = models.CharField(max_length=3, choices=PENGGERAK_RODA_CHOICES, default='2x4')
    tahun = models.IntegerField()
    odometer = models.IntegerField()
    bahanbakar = models.CharField(max_length=10, choices=[
        ('0', 'SOLAR'),
        ('1', 'BENSIN'),
    ], default='BENSIN')
    transmisi = models.CharField(max_length=10, choices=[
        ('0', 'AUTOMATIC'),
        ('1', 'MANUAL')
    ], default='MANUAL')
    kapasitas_mesin = models.CharField(max_length=7, choices=KAPASITAS_MESIN_CHOICES)
    warna = models.CharField(max_length=20)
    harga = models.IntegerField()
    kelayakan = models.CharField(max_length=11, choices=[
        ('1', 'LAYAK'),
        ('0', 'TIDAK LAYAK')
    ], default='TIDAK LAYAK')
     

    def __str__(self):
        return f"{self.merek} - {self.jenis} - {self.transmisi}"
    
    

from django.db.models import CharField
from django.db.models import TextField

from django.db import models as models

# Create your models here.

class Barang(models.Model):
    image = models.ImageField(upload_to = 'images')
    nama_barang = models.CharField(max_length=255)
    harga_barang = models.CharField(max_length=255)
    deskripsi_barang = models.TextField()

    def __str__(self):
        return self.nama_barang
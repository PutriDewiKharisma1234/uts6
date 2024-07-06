from django.db import models

class Produk(models.Model):
    nama = models.CharField(max_length=100)
    deskripsi = models.TextField()
    harga = models.DecimalField(max_digits=100, decimal_places=2)
    stok = models.IntegerField()

    def __str__(self):
        return self.nama
    
class Pelanggan(models.Model):
    nama = models.CharField(max_length=100)
    alamat = models.TextField()
    nomor_telepon = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nama
    
class Pesanan(models.Model):
    produk = models.ForeignKey(Produk, on_delete=models.CASCADE)
    pelanggan = models.ForeignKey(Pelanggan, on_delete=models.CASCADE)
    jumlah = models.IntegerField()
    total_harga = models.DecimalField(max_digits=100, decimal_places=2)
    tanggal_pesanan = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.produk
    
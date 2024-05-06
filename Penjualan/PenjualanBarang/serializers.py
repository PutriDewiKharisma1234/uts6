from rest_framework import serializers
from .models import Produk, Pelanggan, Pesanan

# buat kelas serializer
class ProdukSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produk
        fields = ["nama", "deskripsi", "harga", "stok"]

class PelangganSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelanggan
        fields = ["nama", "alamat", "nomor_telepon", "email"]

class PesananSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pesanan
        fields = ["produk", "pelanggan", "jumlah", "total_harga", "tanggal_pesanan"]
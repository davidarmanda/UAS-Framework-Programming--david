from django.db import models

# Create your models here.
class Jenis(models.Model):
    nama=models.CharField(max_length=50)
    ket=models.TextField()

    def __str__(self):
        return self.nama

class Barang(models.Model):
    kodebrg = models.CharField(max_length=8, default='BRG')
    nama = models.CharField(max_length=50)
    stok = models.IntegerField()
    harga = models.BigIntegerField()
    link_gbr = models.CharField(max_length=150, blank=True)
    waktu_posting=models.DateTimeField(auto_now_add=True)
    jenis_id=models.ForeignKey(Jenis,on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return "{}.{}.{}.{}.{}.{}".format(self.kodebrg,self.nama, self.stok,self.harga,self.link_gbr, self.waktu_posting)

class Transaksi(models.Model):
    kodetrans = models.CharField(max_length=10)
    tgltrans = models.DateTimeField(auto_now_add=True)
    total=models.BigIntegerField()

    def __str__(self):
        return "{}. {}.{}".format(self.kodetrans, self.tgltrans,self.total)

class Detailtrans(models.Model):
    kodetrans = models.CharField(max_length=10)
    kodebrg = models.CharField(max_length=8)
    qty=models.IntegerField()
    subtotal=models.BigIntegerField()


    def __str__(self):
        return "{}. {}".format(self.kodetrans, self.kodebrg)

 #presentasi

class Datapenjualan(models.Model):
    no = models.IntegerField()
    produk = models.CharField(max_length=20)
    kategori = models.CharField(max_length=15)
    merk = models.CharField(max_length=20)
    totalunit = models.IntegerField()
    totalpenjualan = models.BigIntegerField()

    def __str__(self):
        return "{}.{}.{}.{}.{}.{}".format(self.no, self.produk, self.kategori, self.merk, self.totalunit, self.totalpenjualan)

class Datapelanggan(models.Model):
    no = models.IntegerField()
    nama = models.CharField(max_length=20)
    jenispembelian = models.CharField(max_length=20)
    tglbeli = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}.{}.{}".format(self.no, self.nama, self.jenispembelian, self.tglbeli)
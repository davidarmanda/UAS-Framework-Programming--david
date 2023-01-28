from django.contrib import admin

# Register your models here.
from .models import Barang, Jenis
from .models import Transaksi
from .models import Detailtrans
#presentasi
from .models import Datapenjualan
from .models import Datapelanggan

class kolomBarang(admin.ModelAdmin):
    list_display = ['kodebrg','nama','stok','harga','link_gbr','jenis_id']
    search_fields= ['kodebrg','nama']
    list_filter= ('jenis_id',)
    list_per_page= 5
#presentasi
class kolomDatapenjualan(admin.ModelAdmin):
    list_display = ['no','produk','kategori','merk','totalunit','totalpenjualan']
    search_fields= ['no','produk','kategori','merk','totalunit','totalpenjualan']
    list_filter= ('totalunit',)
    list_per_page= 5
    
class kolomDatapelanggan(admin.ModelAdmin):
    list_display = ['no','nama','jenispembelian','tglbeli']
    search_fields= ['no','nama','jenispembelian','tglbeli']
    list_filter= ('nama',)
    list_per_page= 5

admin.site.register(Barang, kolomBarang)
admin.site.register(Jenis)
admin.site.register(Transaksi)
admin.site.register(Detailtrans)
#presentasi
admin.site.register(Datapenjualan, kolomDatapenjualan)
admin.site.register(Datapelanggan, kolomDatapelanggan)


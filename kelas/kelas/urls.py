from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render
from dashboard.views import blog
from dashboard.views import blogdetail
from dashboard.views import contact
from dashboard.views import projectdetail
from dashboard.views import *

#presentasi
from dashboard.views import Penjualan_view
from dashboard.views import Pelanggan_view

def satu(request):
    titelnya="Home"
    konteks = {
            'titel':titelnya,
        }
    return render(request,'home.html',konteks)

urlpatterns = [
    path('admin', admin.site.urls),
    path('',satu),
    path('home/',satu),
    path('blog/',blog),
    path('blogdetail/',blogdetail),
    path('contact/',contact),
    path('projectdetail/',projectdetail),
    path('registrasibrg/', tambah_barang),
    path('regjual/', tambah_penjualan),
    path('regpelanggan/', tambah_pelanggan),
    path('databarang/',Barang_view),
    path('ubah/<int:id_barang>',ubah_brg,name='ubah_brg'),
    path('hapus/<int:id_barang>',hapus_brg,name='hapus_brg'),
    path('ubahjual/<int:id_datapenjualan>',ubah_jual,name='ubah_jual'),
    path('hapusjual/<int:id_datapenjualan>',hapus_jual,name='hapus_jual'),
    path('ubahlg/<int:id_datapelanggan>',ubah_lg,name='ubah_lg'),
    path('hapuslg/<int:id_datapelanggan>',hapus_lg,name='hapus_lg'),
    #presentasi
    path('datapenjualan/',Penjualan_view),
    path('datapelanggan/',Pelanggan_view),
]

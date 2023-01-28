from django.shortcuts import render, redirect
from dashboard.forms import FormBarang, FormDatapenjualan, FormDatapelanggan
from dashboard.models import Barang, Datapelanggan, Datapenjualan
from django.contrib import messages

#presentasi
from dashboard.models import Datapenjualan
from dashboard.models import Datapelanggan
# # Create your views here.
#presentasi
def Pelanggan_view(request):
    datapelanggans=Datapelanggan.objects.all()
    titelnya="Data Pelanggan"
    konteks={
        'datapelanggan':datapelanggans,
        'titel':titelnya,
    } 
    return render(request, 'datapelanggan.html', konteks)

def Penjualan_view(request):
    datapenjualans=Datapenjualan.objects.all()
    titelnya="Data Penjualan"
    konteks={
        'datapenjualan':datapenjualans,
        'titel':titelnya,
    }
    return render(request, 'datapenjualan.html', konteks)

def Barang_view(request):
    barangs=Barang.objects.all()
    titelnya="Data Barang"
    konteks={
        'barang':barangs,
        'titel':titelnya, 
    }
    return render(request, 'tampil_brg.html',konteks)

def tambah_barang(request):
    if request.POST:
        form= FormBarang(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil Ditambahkan")
            form=FormBarang()
            titelnya="Registrasi"
            konteks={
                'form':form,
                'titel':titelnya,
            }
            return render(request,'tambah_barang.html',konteks)
    else:
        form=FormBarang()
        konteks = {
            'form':form,
        }
    return render(request,'tambah_barang.html',konteks)

def tambah_pelanggan(request):
    if request.POST:
        form= FormDatapelanggan(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil Ditambahkan")
            form=FormDatapelanggan()
            titelnya="Registrasi"
            konteks={
                'form':form,
                'titel':titelnya,
            }
            return render(request,'tambah_pelanggan.html',konteks)
    else:
        form=FormDatapelanggan()
        konteks = {
            'form':form,
        }
    return render(request,'tambah_pelanggan.html',konteks)

def tambah_penjualan(request):
    if request.POST:
        form= FormDatapenjualan(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil Ditambahkan")
            form=FormDatapenjualan()
            titelnya="Registrasi"
            konteks={
                'form':form,
                'titel':titelnya,
            }
            return render(request,'tambah_penjualan.html',konteks)
    else:
        form=FormDatapenjualan()
        konteks = {
            'form':form,
        }
    return render(request,'tambah_penjualan.html',konteks)

def hapus_brg(request, id_barang):
    barangs=Barang.objects.filter(id=id_barang)
    barangs.delete()
    barangs=Barang.objects.all()
    titelnya="Data Barang"
    konteks={
        'barang':barangs,
        'titel':titelnya, 
    }
    messages.success(request,"Data Terhapus")
    return render(request,'tampil_brg.html', konteks)

def hapus_jual(request, id_datapenjualan):
    datapenjualans=Datapenjualan.objects.filter(id=id_datapenjualan)
    datapenjualans.delete()
    datapenjualans=Datapenjualan.objects.all()
    titelnya="Data Penjualan"
    konteks={
        'datapenjualan':datapenjualans,
        'titel':titelnya, 
    }
    messages.success(request,"Data Terhapus")
    return render(request,'datapenjualan.html', konteks)

def hapus_lg(request, id_datapelanggan):
    datapelanggans=Datapelanggan.objects.filter(id=id_datapelanggan)
    datapelanggans.delete()
    datapelanggans=Datapelanggan.objects.all()
    titelnya="Data Pelanggan"
    konteks={
        'datapelanggan':datapelanggans,
        'titel':titelnya, 
    }
    messages.success(request,"Data Terhapus")
    return render(request,'datapelanggan.html', konteks)

def ubah_brg(request, id_barang):
    barangs=Barang.objects.get(id=id_barang)
    if request.POST:
        form=FormBarang(request.POST,instance=barangs)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil diubah")
            return redirect('ubah_brg',id_barang=id_barang)
    else:
        form=FormBarang(instance=barangs)
        konteks = {
            'form':form,
            'barangs': barangs
        }
    return render(request,'ubah_brg.html',konteks)

def ubah_jual(request, id_datapenjualan):
    datapenjualans=Datapenjualan.objects.get(id=id_datapenjualan)
    if request.POST:
        form=FormDatapenjualan(request.POST,instance=datapenjualans)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil diubah")
            return redirect('ubah_jual',id_datapenjualan=id_datapenjualan)
    else:
        form=FormDatapenjualan(instance=datapenjualans)
        konteks = {
            'form':form,
            'datapenjualans': datapenjualans
        }
    return render(request,'ubah_jual.html',konteks)

def ubah_lg(request, id_datapelanggan):
    datapelanggans=Datapelanggan.objects.get(id=id_datapelanggan)
    if request.POST:
        form=FormDatapelanggan(request.POST,instance=datapelanggans)
        if form.is_valid():
            form.save()
            messages.success(request,"Data Berhasil diubah")
            return redirect('ubah_lg',id_datapelanggan=id_datapelanggan)
    else:
        form=FormDatapelanggan(instance=datapelanggans)
        konteks = {
            'form':form,
            'datapelanggans': datapelanggans
        }
    return render(request,'ubah_lg.html',konteks)

def blog(request):
    titelnya="Blog"
    konteks = {
            'titel':titelnya,
        }
    return render(request,'blog.html',konteks)

def blogdetail(request):
    titelnya="Blog Detail"
    konteks = {
            'titel':titelnya,
        }
    return render(request,'blog-detail.html',konteks)

def contact(request):
    titelnya="Contact"
    konteks = {
            'titel':titelnya,
        }
    return render(request,'contact.html',konteks)

def projectdetail(request):
    titelnya="Project Detail"
    konteks = {
            'titel':titelnya,
        }
    return render(request,'project-detail.html',konteks)
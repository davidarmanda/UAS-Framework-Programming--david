from django.forms import ModelForm
from dashboard.models import Barang, Datapelanggan, Datapenjualan
from django import forms

class FormBarang(ModelForm):
    class Meta :
        model=Barang
        fields='__all__'

        widgets = {
            'kodebrg' : forms.TextInput({'class':'form-control'}),
            'nama' : forms.TextInput({'class':'form-control'}),
            'stok' : forms.NumberInput({'class':'form-control'}),
            'harga' : forms.NumberInput({'class':'form-control'}),
            'link_gbr' : forms.TextInput({'class':'form-control'}),
            'jenis_id' : forms.Select({'class':'form-control'}),
        }
        
class FormDatapenjualan(ModelForm):
    class Meta :
        model=Datapenjualan
        fields='__all__'

        widgets = {
            'no' : forms.TextInput({'class':'form-control'}),
            'produk' : forms.TextInput({'class':'form-control'}),
            'kategori' : forms.TextInput({'class':'form-control'}),
            'merk' : forms.TextInput({'class':'form-control'}),
            'totalunit' : forms.NumberInput({'class':'form-control'}),
            'totalpenjualan' : forms.NumberInput({'class':'form-control'}),
        }
class FormDatapelanggan(ModelForm):
    class Meta :
        model=Datapelanggan
        fields='__all__'

        widgets = {
            'no' : forms.TextInput({'class':'form-control'}),
            'nama' : forms.TextInput({'class':'form-control'}),
            'jenispembelian' : forms.TextInput({'class':'form-control'}),
            'tglbeli' : forms.NumberInput({'class':'form-control'}),
        }
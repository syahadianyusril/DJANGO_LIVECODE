from django import forms

from .models import Barang

class PostForm(forms.ModelForm):

    class Meta:
        model = Barang
        fields = ('image','nama_barang','harga_barang','deskripsi_barang')
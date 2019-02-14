from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import Barang
from .forms import PostForm
# Create your views here.

def barang(request):
    barang = Barang.objects.all()
    return render(request, 'barang/barang.html',{'barangs':barang})

def barang_detail(request, post_id):
    detail_barang = get_list_or_404(Barang, id=post_id)
    return render(request, 'barang/detail_barang.html', {'barangs': detail_barang})

def form(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('barang')
    else:
        form = PostForm()
    return render(request,'barang/input_barang.html', {'form': form})
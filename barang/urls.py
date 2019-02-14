from django.urls import path
from . import views

urlpatterns = [
    path('', views.barang, name='barang'),
    path('barang/<int:post_id>/', views.barang_detail, name="barang_detail"),
    path('input_barang/', views.form, name='form'),
]
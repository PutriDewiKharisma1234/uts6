from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('produk/', views.ProdukList.as_view()),
    path('produk/<int:pk>/', views.ProdukDetail.as_view()),
    path('Pelanggan/', views.PelangganList.as_view()),
    path('Pelanggan/<int:pk>/', views.PelangganDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
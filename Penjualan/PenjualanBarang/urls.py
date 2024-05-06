from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('Produk/', views.ProdukList.as_view()),
    path('Produk/<int:pk>/', views.ProdukDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
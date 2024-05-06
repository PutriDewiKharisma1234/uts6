from rest_framework import status, permissions
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from .models import  Produk
from .serializers import ProdukSerializer

# view untuk produk dengan class base view
class ProdukList(APIView):
    """
    ini merupakan proses pengambilan data atau simpan data
    """
    permission_classes = [permissions.AllowAny]
    def get(self, request, format=None):
        produk = Produk.objects.all()
        serializer = ProdukSerializer(produk, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ProdukSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProdukDetail(APIView):
    """
    ambil data, edit atau hapus data
    """
    parser_classes = [permissions.AllowAny]
    def get_object(self, pk):
        try:
            return Produk.objects.get(pk=pk)
        except Produk.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        Produk = self.get_object(pk)
        serializer = ProdukSerializer(Produk)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        Produk = self.get_object(pk)
        serializer = ProdukSerializer(Produk, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        Produk = self.get_object(pk=pk)
        Produk.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
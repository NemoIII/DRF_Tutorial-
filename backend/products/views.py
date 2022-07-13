from rest_framework import generics

from .models import Products
from .serializers import ProductsSerializer


class ProductCreateAPIView(generics.CreateAPIView):
  queryset = Products.objects.all()
  serializers_class = ProductsSerializer

product_create_view = ProductCreateAPIView.as_view()

class ProductDetailAPIView(generics.RetrieveAPIView):
  queryset = Products.objects.all()
  serializers_class = ProductsSerializer
  #lookup_field = 'pk' 

product_detail_view = ProductDetailAPIView.as_view()
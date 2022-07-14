from rest_framework import generics

from .models import Products
from .serializers import ProductsSerializer


class ProductCreateAPIView(generics.CreateAPIView):
  queryset = Products.objects.all()
  serializer_class = ProductsSerializer

  def perform_create(self, serializer):
    print(serializer.validated_data)
    title = serializer.validated_data.get('title')
    content = serializer.validated_data.get('content') or None
    if content is None:
      content = title
    serializer.save(content=content)

product_create_view = ProductCreateAPIView.as_view()

class ProductDetailAPIView(generics.RetrieveAPIView):
  queryset = Products.objects.all()
  serializer_class = ProductsSerializer
  #lookup_field = 'pk' 

product_detail_view = ProductDetailAPIView.as_view()
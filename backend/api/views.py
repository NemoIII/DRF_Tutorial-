from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Products
from products.serializers import ProductsSerializer


@api_view(["POST"])
def api_home(request, *args, ** kwargs):
  serializer = ProductsSerializer(data=request.data)
  if serializer.is_valid():
    print(serializer)
    data = serializer.data
  return Response(data)
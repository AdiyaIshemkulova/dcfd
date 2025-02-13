from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.viewsets import ViewSet, ModelViewSet
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAdminUser, IsAuthenticated,IsAuthenticatedOrReadOnly

from .models import Product,Category
from .serializers import ProductSerializer

# @api_view(['GET'])
# def get_products(request):
#     products = Product.objects.all()
#     serializer = ProductSerializer(data=products, many = True)
#     serializer.is_valid()
#     return Response(serializer.data)


# @api_view(['GET'])
# def get_product(request,id):
#     #product = Product.objects.get(id=id)
#     product = get_object_or_404(Product, id=id)

#     serializer = ProductSerializer(instance=product)
#     return Response(serializer.data)


# @api_view(['POST'])
# def create_product(request):
#     data = request.data
#     #category = get_object_or_404(Category,id=data['category'])
    
#     serializer = ProductSerializer(data=data)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save()

#     return Response(201)

# @api_view(['DELETE'])
# def delete_product(request,id):
#     product = get_object_or_404(Product, id=id)
#     product.delete()
#     return Response(status=204)

# @api_view(['PUT','PATCH'])
# def update_product(request,id):
#     if request.method == 'PUT':
#         product = get_object_or_404(Product, id=id)
#         serializer = ProductSerializer(instance=product, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#     elif request.method == 'PATCH':
#         product = get_object_or_404(Product,id=id)
#         serializer = ProductSerializer(instance=product, data=request.data,partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#     return Response(201)


# class ProductVievSet(ViewSet):
#     def list(self, request):
#         ...

#     def retrieve(self,request, pk=None): #GET, определенный товар
#         ...

#     def update(self, request, pk=None): #PUT, полное обновление данных
#         ...

#     def partial_update(self, request, pk=None): #PATCH, частичное обновление
#         ...

#     def destroy(self,request, pk=None): #DELETE, удаление
#         ...

#     def create(self,reqquest, pk=None): #POST, создание
#         ...


class ProductModelVeiwSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    
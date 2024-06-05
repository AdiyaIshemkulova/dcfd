from django.urls import path, include

from rest_framework.routers import DefaultRouter

# from .views import get_products,get_product,create_product, update_product, delete_product

from .views import ProductModelViewSet

router = DefaultRouter()
#router.register('product', ProductVievSet)
router.register('product', ProductModelViewSet)


urlpatterns = [
    # path('get_products/', get_products),
    # path('get_product/<int:id>/', get_product),
    # path('create_product/',create_product),
    # path('update_product/<int:id>/', update_product),
    # path('delete_product/<int:id>/',delete_product)
    path('',include(router.urls))
]
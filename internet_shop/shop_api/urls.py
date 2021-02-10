from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from shop_api.views import ProductViewSet, ReviewViewSet, OrderViewSet, PositionViewSet, CollectionViewSet, \
    AddProductToCollectionViewSet

urlpatterns = format_suffix_patterns([
    path('products/', ProductViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('products/<int:pk>/', ProductViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('product-reviews/', ReviewViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('orders/', OrderViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('orders/<int:pk>/', OrderViewSet.as_view({'get': 'retrieve'})),
    path('positions/', PositionViewSet.as_view({'post': 'create'})),
    path('product-collections/', CollectionViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('product-collections/<int:pk>/', CollectionViewSet.as_view({'get': 'retrieve'})),
    path('product-to-collection/', AddProductToCollectionViewSet.as_view({'post': 'create'}))
])

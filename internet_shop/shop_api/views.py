from django.db import transaction
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from shop_api.filters import ProductFilter, ReviewFilter, OrderFilter
from shop_api.models import Product, Review, Order, Position, ProductCollections, ProductListForCollection

from shop_api.serializers import ProductSerializer, ProductDetailSerializer, \
    ReviewCreateSerializer, ReviewSerializer, OrderSerializer, OrderCreateSerializer, \
    PositionCreateSerializer, OrderDetailSerializer, CollectionsSerializer, CollectionsCreateSerializer, \
    AddProductToCollectionSerializer, CollectionsDetailSerializer, ReviewUpdateSerializer


class ProductViewSet(ModelViewSet):
    """ViewSet для продуктов """

    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilter
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "create", "update"]:
            return ProductSerializer
        elif self.action == "retrieve":
            return ProductDetailSerializer

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAdminUser()]
        return []


class ReviewViewSet(ModelViewSet):
    """ViewSet для отзывов """

    filter_backends = (DjangoFilterBackend,)
    filterset_class = ReviewFilter
    queryset = Review.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return ReviewSerializer
        elif self.action == "create":
            return ReviewCreateSerializer
        elif self.action == "update":
            return ReviewUpdateSerializer

    def get_permissions(self):
        if self.action in ["create"]:
            return [IsAuthenticated()]
        return []

    @transaction.atomic
    def destroy(self, request, *args, **kwargs):
        review_user = request.user
        instance = self.get_object()
        review_creator = instance.creator

        if review_user != review_creator:
            raise ValidationError({"Review": "Удалять можно только свои записи!"})
        return super().destroy(request, *args, **kwargs)

    @transaction.atomic
    def update(self, request, *args, **kwargs):
        review_user = request.user
        instance = self.get_object()
        review_creator = instance.creator
        if review_user != review_creator:
            raise ValidationError({"Review": "Обновлять можно только свои записи!"})
        return super().update(request, *args, **kwargs)


class OrderViewSet(ModelViewSet):
    """ViewSet для заказов """

    filter_backends = (DjangoFilterBackend,)
    filterset_class = OrderFilter
    queryset = Order.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return OrderSerializer
        elif self.action == "create":
            return OrderCreateSerializer
        elif self.action == "retrieve":
            return OrderDetailSerializer
        elif self.action == "update":
            return OrderCreateSerializer

    def get_permissions(self):
        if self.action in ["create", "destroy"]:
            return [IsAuthenticated()]
        elif self.action in ["list", "update"]:
            return [IsAdminUser()]
        return []

    @transaction.atomic
    def retrieve(self, request, *args, **kwargs):
        order_user = request.user
        instance = self.get_object()
        order_creator = instance.user
        if order_user != order_creator:
            raise ValidationError({"Order": "Просматривать можно только свои заказы!"})
        return super().retrieve(request, *args, **kwargs)


class PositionViewSet(ModelViewSet):
    """ViewSet для позиций в заказах """

    queryset = Position.objects.all()
    serializer_class = PositionCreateSerializer

    def get_permissions(self):
        if self.action in ["create", "partial_update", "destroy"]:
            return [IsAuthenticated()]
        if self.action == "list":
            return [IsAdminUser()]
        return []


class CollectionViewSet(ModelViewSet):
    """ViewSet для подборок """

    queryset = ProductCollections.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return CollectionsSerializer
        elif self.action == "create":
            return CollectionsCreateSerializer
        elif self.action == "retrieve":
            return CollectionsDetailSerializer

    def get_permissions(self):
        if self.action == "create":
            return [IsAdminUser()]
        return []


class AddProductToCollectionViewSet(ModelViewSet):
    """ViewSet для добавления товаров в подборки """

    queryset = ProductListForCollection.objects.all()
    serializer_class = AddProductToCollectionSerializer

    def get_permissions(self):
        if self.action in ["create", "destroy"]:
            return [IsAdminUser()]
        return []

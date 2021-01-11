from rest_framework import generics, permissions
from .serializers import ProductSerializer, ProductCompleteSerializer
from .models import Product
from django.utils import timezone
from django.contrib.auth.models import User

class ProductSoldoutList(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Product.objects.filter(user=user, qty = 0)


class ProductAvailableList(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        #return Product.objects.filter(user=user, qty__isnull=False)
        return Product.objects.filter(user=user).exclude(qty=0)


class ProductListCreate(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Product.objects.filter(user=user, dateupdated__isnull=True)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Product.objects.filter(user=user)

class ProductComplete(generics.UpdateAPIView):
    serializer_class = ProductCompleteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Product.objects.filter(user=user)

    def perform_update(self, serializer):
        serializer.instance.dateupdated = timezone.now()
        serializer.save()

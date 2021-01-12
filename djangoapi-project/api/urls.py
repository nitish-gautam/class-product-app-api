from django.urls import path

from . import views

urlpatterns = [
    # Product
    path('api/products', views.ProductListCreate.as_view()),
    path('api/products/<int:pk>', views.ProductRetrieveUpdateDestroy.as_view()),
    path('api/products/soldout', views.ProductSoldoutList.as_view()),
    path('api/products/available', views.ProductAvailableList.as_view())
]
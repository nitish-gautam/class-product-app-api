from django.urls import path

from . import views

urlpatterns = [
    # Product
    path('api/products', views.ProductListCreate.as_view()),
    path('api/products/<int:pk>', views.ProductRetrieveUpdateDestroy.as_view()),
    path('api/products/<int:pk>/complete', views.ProductComplete.as_view()),
    path('api/products/soldout', views.ProductCompletedList.as_view())
]
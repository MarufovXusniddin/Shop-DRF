from django.urls import path
from .views import CategoryAPI, CategoryDetailAPI, ProductAPI, ProductDetailAPI, ReviewAPI, ReviewDetailAPI

urlpatterns = [
    path('categories/', CategoryAPI.as_view()),
    path('category/<int:pk>/', CategoryDetailAPI.as_view()),

    path('products/', ProductAPI.as_view()),
    path('product/<int:pk>/', ProductDetailAPI.as_view()),

    path('reviews/', ReviewAPI.as_view()),
    path('review/<int:pk>/', ReviewDetailAPI.as_view())
]

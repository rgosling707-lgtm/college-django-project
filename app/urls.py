from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.homeView, name="home_view"),
    path('index/', views.indexView, name="index_view"),
    path('products/', views.productsView, name="products_view"),
]
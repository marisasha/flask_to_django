from django.contrib import admin
from django.urls import path , include
from django_app import views

urlpatterns = [
    path('', views.home),
    path('autarization', views.autarization),
    path('product', views.product),
    path('product_info/<int:product_id>', views.product_info),
]

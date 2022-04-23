from socket import fromfd
from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('translated/', views.translated, name='translated'),
    path('', views.HomePageView, name='home'),
    path('about/', views.AboutPageView, name='about'),
    path('products/', views.ProductsPageView, name='products'),
    path('', views.translater, name='translater'),
]

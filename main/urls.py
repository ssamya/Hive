from django.contrib import admin
from django.urls import path, include
from main import views
from django.conf.urls.static import static
from django.conf import settings
from . import views


app_name='main'

urlpatterns = [
    path('', views.popular_list, name='popular_list'),
    path('shop/', views.product_list, name='product_list'),
    path('shop/<slug:slug>/', views.product_detail, name='product_detail'),
    path('order_time_page/', views.order_time_page, name='order_time_page'),
    path('thanks/', views.thanks_page, name='thanks_page'),
    path('shop/category/<slug:category_slug>/', views.product_list,
        name='product_list_by_category'),
]

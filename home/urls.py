from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("shop", views.shop, name="shop"),
    path("filter-category",views.filter_category,name="filter_category"),
    path("product/<str:slug>",views.product_details,name="product_details"),
    path("user-account",views.user_account,name="user_account"),
]

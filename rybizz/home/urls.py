from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),  
    path("product", views.product, name="product"),
    path("product_cpy", views.product_cpy, name="product_cpy"), 
   
    

]
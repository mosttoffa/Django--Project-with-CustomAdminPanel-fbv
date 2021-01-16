from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^product/productpage/$', views.product_page, name='product_page'),    
   
]



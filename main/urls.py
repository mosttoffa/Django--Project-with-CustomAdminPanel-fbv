from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.home, name='home'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^product/$', views.product, name='product'),
    url(r'^product_detail/$', views.product_detail, name='product_detail'),
  
  
]

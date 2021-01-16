from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^product/<slug:category_slug>/$', views.product_show, name='product_show'),
    url(r'^product/productpage/$', views.product_page, name='product_page'),    
    url(r'^panel/products/productadd/$', views.product_add, name='product_add'),   
    url(r'^panel/products/productlist/$', views.product_list, name='product_list'),    
 
    url(r'^export/products/csv/$', views.export_product_csv, name='export_product_csv'),    
    url(r'^import/products/csv/$', views.import_product_csv, name='import_product_csv'),    

]


from django.contrib import admin
from django.urls import path, re_path
from products.views import products_home, product_detail,add_product,import_export
from warehouse.views import home_page_redirect


urlpatterns = [


    path('', products_home),
    path('update/',add_product),
    path('import_export/',import_export),
    #/products/123/
    re_path('^(?P<product_id>[0-9]{1})/$',product_detail)
]
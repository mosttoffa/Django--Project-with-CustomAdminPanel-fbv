from django.contrib import admin
from .models import Categori, Products 

# Register your models here.

class CategoriAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'image']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Categori, CategoriAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'image', 'stock', 'available']
    list_editable =[ 'price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 5

admin.site.register(Products, ProductAdmin)

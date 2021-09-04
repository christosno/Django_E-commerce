from django.contrib import admin
from .models import Products, Order
# Register your models here.

admin.site.site_header = "E-commerce site"
admin.site.title = "EBC shop"
admin.site.index_title = "Manage EBC shoping"

admin.site.register(Products)
admin.site.register(Order)

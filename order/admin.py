from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'customer', 'item')


# Register your models here.
admin.site.register(Order)

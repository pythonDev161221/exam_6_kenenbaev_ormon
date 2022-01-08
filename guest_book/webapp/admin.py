from django.contrib import admin
from .models import Customer


# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['pk', 'customer_name', 'order_text']
    list_filter = ['customer_name']
    search_fields = ['customer_name', 'order_text']
    fields = ['customer_name', 'order_text']


admin.site.register(Customer, CustomerAdmin)

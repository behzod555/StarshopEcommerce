from django.contrib import admin

from .models import *

class ProductAdmin(admin.ModelAdmin):
	list_display = ('name','category','price')
	list_filter = ['name','category']
	search_fields = ['name']
class CustomerAdmin(admin.ModelAdmin):
	list_display = ['name','email']
	search_fields = ['name']
class OrderItemAdmin(admin.ModelAdmin):
	list_display = ['order','product','quantity']
	search_fields = ['order']

class OrderAdmin(admin.ModelAdmin):
	list_display = ['id', 'customer','tel','city','address','complete']
	list_filter = ['complete']
	search_fields = ['order']



admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Phone)
admin.site.register(Notebook)

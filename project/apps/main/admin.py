from django.contrib import admin

from main.models import Pen, Customer, Order


class PenAdmin(admin.ModelAdmin):

    model = Pen

    list_display = [
        'title',
        'size',
        'price',
        'count'
    ]
    
class CustomerAdmin(admin.ModelAdmin):

    model = Customer

    list_display = [
        'title',
        'place'
    ]

class OrderAdmin(admin.ModelAdmin):

    model = Order

    list_display = [
        'customer',
        'product',
        'count'
    ]


admin.site.register(Pen, PenAdmin),
admin.site.register(Customer, CustomerAdmin),
admin.site.register(Order, OrderAdmin)
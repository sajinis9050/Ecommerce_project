#
from django.contrib import admin
from . models import Product, Offer, Home, Cart, Chat


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'description', 'discount')


class HomeAdmin(admin.ModelAdmin):
    list_display = ('message', 'special', 'notes')


class CartAdmin(admin.ModelAdmin):
    list_display = ('instruction', 'note')


class ChatAdmin(admin.ModelAdmin):
    list_display = ('display', 'submit')


admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OfferAdmin)
admin.site.register(Home, HomeAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Chat, ChatAdmin)
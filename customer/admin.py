from django.contrib import admin

from .models import CustomerModel, AddressModel


# Register your models here.
# admin.site.register(Article)

@admin.register(CustomerModel)
class CustomerAdmin(admin.ModelAdmin):
    list_filter = ('first_name', 'last_name')
    list_display = ('first_name', 'last_name')


@admin.register(AddressModel)
class AddressAdmin(admin.ModelAdmin):
    list_filter = ('street', 'city')
    list_display = ('street', 'city')

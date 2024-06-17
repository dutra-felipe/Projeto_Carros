from django.contrib import admin
from cars.models import Cars, Brand

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('model', 'brand__name',)

admin.site.register(Brand, BrandAdmin)
admin.site.register(Cars, CarAdmin)

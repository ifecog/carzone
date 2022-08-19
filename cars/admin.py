from django.contrib import admin
from .models import Car
from django.utils.html import format_html

# Register your models here.


class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.car_photo.url))

    thumbnail.short_description = 'photo'

    list_display = ('id', 'thumbnail', 'car_title', 'city', 'color',
                    'model', 'year', 'body_style', 'fuel_type', 'is_featured')
    list_display_links = ('id', 'car_title', 'thumbnail')
    search_fields = ('car_title', 'model', 'body_type')
    list_filter = ('city', 'model', 'body_style', 'fuel_type')


admin.site.register(Car, CarAdmin)

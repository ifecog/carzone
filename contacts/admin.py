from django.contrib import admin
from .models import Contact

# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name',
                    'car_title', 'city', 'email', 'date_sent')
    list_display_links = ('id', 'first_name', 'email')
    search_fields = ('first_name', 'last_name', 'car_title', 'email')
    list_per_page = 25


admin.site.register(Contact, ContactAdmin)

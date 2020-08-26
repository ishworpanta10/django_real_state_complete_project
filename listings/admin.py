from django.contrib import admin
from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published',
                    'price', 'list_date', 'realtors',)  # for displaying data table in admin area

    list_display_links = ('id', 'title',)  # to navigate by clicking

    list_filter = ('realtors', 'list_date',)  # for filter in admin area

    list_editable = ('is_published',)   # for editing row from table itself

    search_fields = ('title', 'description', 'address',
                     'city', 'zipcode', 'state', 'price')  # for displaying search field in admin area

    list_per_page = 20  # pagination 20 per page


admin.site.register(Listing, ListingAdmin)

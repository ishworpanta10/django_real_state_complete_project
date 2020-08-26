from django.contrib import admin
from .models import Realtor


class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'is_mvp', 'hire_date')

    list_display_links = ('id', 'name')

    search_fields = ('name', 'email', 'phone')

    list_editable = ('is_mvp',)

    list_per_page = 20

    list_filter = ('hire_date',)


admin.site.register(Realtor, RealtorAdmin)

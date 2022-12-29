from django.contrib import admin

from .models import Mrc, Municipalite
# tabular inline recipes


class MunicipaliteInline(admin.TabularInline):
    model = Municipalite
    extra = 2  # how many rows to show


class MrcAdmin(admin.ModelAdmin):
    search_fields = ['name']
    inlines = [MunicipaliteInline]


class MunicipaliteAdmin(admin.ModelAdmin):
    autocomplete_fields = ['mrc']
    list_display = ['name', 'mrc']
    list_per_page = 15
    search_fields = ['name']


admin.site.register(Mrc, MrcAdmin)
admin.site.register(Municipalite, MunicipaliteAdmin)

from django.contrib import admin

from .models import Habitat, SousHabitat
# tabular inline recipes


class SousHabitatInline(admin.TabularInline):
    model = SousHabitat
    extra = 5  # how many rows to show


class HabitatAdmin(admin.ModelAdmin):
    search_fields = ['habitat']
    inlines = [SousHabitatInline]


class SousHabitatAdmin(admin.ModelAdmin):
    autocomplete_fields = ['habitat']
    list_display = ['habitat', 'sous_habitat']


admin.site.register(Habitat, HabitatAdmin)
admin.site.register(SousHabitat, SousHabitatAdmin)

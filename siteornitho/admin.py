from django.contrib import admin
# from django import forms
from .models import SiteOrnitho, SiteOrnithoImage


class SiteOrnithoAdmin(admin.ModelAdmin):
    autocomplete_fields = ['municipalite']
    list_display = ['nom_du_site', 'municipalite', 'miseajour','status']
    list_per_page = 15

    fieldsets = (
        (None, {
            'fields': ('nom_du_site', 'description_generale', 'periode_interet_debut', 'periode_interet_fin','status')
        }),
        ('Géographie', {
            'fields': ('locid', 'longitude', 'latitude', 'municipalite', 'sous_habitat')
        }),
        ('Facilités', {
            'fields': ('toilette', 'banc', 'picnique', 'transport', 'acces_gratuit',)
        }),
        ('Information additionnelle', {
            'fields': ('enjeux', 'bon_a_savoir', 'url', 'stakeholder',)
        }),
        ('Meta donnees', {
            'fields': ('auteur',)
        }),
    )
    # def get_form(self, request, obj=None, **kwargs):
    #     form = super().get_form(request, obj, **kwargs)
    #     form.base_fields["sous_habitat"].label = "SOUS HABITAT"

    #     return form


admin.site.register(SiteOrnitho, SiteOrnithoAdmin)
admin.site.register(SiteOrnithoImage)

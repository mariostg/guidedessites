from django import forms
from .models import SiteOrnitho


class SearchSiteForm(forms.ModelForm):
    class Meta:
        model = SiteOrnitho
        fields = [
            "municipalite",
            "periode_interet_debut",
            "periode_interet_fin",
            "sous_habitat",
            "transport",
        ]
        labels = {
            "periode_interet_debut": "Période d'intéret",
            "periode_interet_fin": "",
            "sous_habitat": "Description de l'habitat",
            "transport": "Transport en commun",
        }

    def __init__(self, *args, **kwargs):
        super(SearchSiteForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "w3-input"})
            field.required = False

        # self.fields["periode_interet_fin"].required = False
        # help_texts = {
        #     "transport": "Transport en commun disponible à proximité",
        # }
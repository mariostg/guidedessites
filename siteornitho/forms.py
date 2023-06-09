from django import forms
from .models import SiteOrnitho, SiteOrnithoImage
from django.forms import widgets


class SearchSiteForm(forms.ModelForm):
    class Meta:
        model = SiteOrnitho
        fields = [
            "nom_du_site",
            "municipalite",
            "periode_interet_debut",
            "periode_interet_fin",
            "sous_habitat",
            "transport",
        ]
        labels = {
            "periode_interet_fin": "",
        }

    def __init__(self, *args, **kwargs):
        super(SearchSiteForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "input"})
            field.required = False


class SiteForm(forms.ModelForm):
    class Meta:
        model = SiteOrnitho
        fields = [
            "nom_du_site",
            "municipalite",
            "locid",
            "longitude",
            "latitude",
            "url",
            "auteur",
            "periode_interet_debut",
            "periode_interet_fin",
            "sous_habitat",
            "description_generale",
            "site_accessible",
            "raison_non_accessible",
            "transport",
            "acces_gratuit",
            "bon_a_savoir",
            "toilette",
            "picnique",
            "banc",
            "enjeux",
            "status",
            "stakeholder",
        ]
        template_name = "siteornitho/site_form.html"

        widgets = {"stakeholder": forms.Textarea(attrs={"rows": 3})}

    # def __init__(self, *args, **kwargs):
    #     super(SiteForm, self).__init__(*args, **kwargs)

    #     for name, field in self.fields.items():
    #         field.widget.attrs.update({"class": "input"})

    def clean_latitude(self):
        latitude = self.cleaned_data["latitude"]
        if latitude > 90:
            self.add_error("latitude", "Latitude ne peux excéder 90")
        if latitude < -90:
            self.add_error("latitude", "Latitude ne peux être inférieure à -90")
        return latitude

    def clean_longitude(self):
        longitude = self.cleaned_data["longitude"]
        if longitude > 180:
            self.add_error("longitude", "Longitude ne peux excéder 180")
        if longitude < -180:
            self.add_error("longitude", "Longitude ne peux être inférieure à -180")
        return longitude

    def clean_locid(self):
        locid = self.cleaned_data["locid"]
        if not locid:
            return locid
        if not locid[0].isalpha():
            self.add_error("locid", "Localisation doit débuter avec une lettre")
        return locid


class ImageForm(forms.ModelForm):
    class Meta:
        model = SiteOrnithoImage
        fields = [
            "siteornitho",
            "title",
            "description",
            "photo_author",
            "photo_date",
            "image",
        ]
        template_name = "siteornitho/image_form.html"

        widgets = {
            "photo_date": forms.DateInput(
                format=("%Y-%m-%d"),
                attrs={
                    "class": "form-control",
                    "placeholder": "Select a date",
                    "type": "date",
                },
            ),
        }

    def __init__(self, *args, **kwargs):
        super(ImageForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "input"})

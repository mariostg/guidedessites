from django import forms
from .models import Mrc, Municipalite


class MrcForm(forms.ModelForm):
    class Meta:
        model = Mrc
        fields = ["name"]
        template_name = "geographie/mrc_form.html"

    def __init__(self, *args, **kwargs):
        super(MrcForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "input"})


class MunicipaliteForm(forms.ModelForm):
    class Meta:
        model = Municipalite
        fields = ["name", "mrc"]
        template_name = "geographie/municipalite_form.html"

    def __init__(self, *args, **kwargs):
        super(MunicipaliteForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "input"})

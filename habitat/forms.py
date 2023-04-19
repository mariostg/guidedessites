from django import forms
from .models import Habitat, SousHabitat


class HabitatForm(forms.ModelForm):
    class Meta:
        model = Habitat
        fields = ["habitat"]
        template_name = "habitat/habitat_form.html"

    def __init__(self, *args, **kwargs):
        super(HabitatForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "input"})


class SousHabitatForm(forms.ModelForm):
    class Meta:
        model = SousHabitat
        fields = ["habitat", "sous_habitat"]
        template_name = "habitat/sous_habitat_form.html"

    def __init__(self, *args, **kwargs):
        super(SousHabitatForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "input"})

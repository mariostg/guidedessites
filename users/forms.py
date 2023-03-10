from django.forms import ModelForm
from .models import UserProfile

class ProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'email', 
                  'location', 'email', 'phone']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
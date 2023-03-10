from django.db import models
from django.contrib.auth.models import User
import uuid
from phone_field import PhoneField #https://pypi.org/project/django-phone-field/

class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True,related_name='profile')
    name = models.CharField(max_length=200, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    phone=PhoneField(blank=True, help_text="Office Phone Number")

    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self):
        return str(self.user.username)
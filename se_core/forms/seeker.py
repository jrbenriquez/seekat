from django import forms
from django.contrib.auth import get_user_model

from se_core.models import Seeker


class SeekerForm(forms.ModelForm):
    class Meta:
        model = Seeker
        fields = ['first_name', 'last_name', 'public_name']


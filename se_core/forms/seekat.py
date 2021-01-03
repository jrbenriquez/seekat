from django import forms
from django.contrib.auth import get_user_model

from se_core.models import Seekat

# Flow
# 1. User types in new or is shown matching Seekats
# 2. User types in new or existing category to group seek
# 3. Next Page
# 3. Additional Details - Seek - Hashtags | Seekat | Parent, description, address or can be skipped
# 4. Seek is saved along with respective seeker_id, category_id, seekat_id


class NewSeekForm(forms.Form):
    seekat_id = forms.IntegerField(required=False)
    seekat_name = forms.CharField(max_length=100)
    category_id = forms.IntegerField(required=False)
    category = forms.CharField(max_length=100)


class SeekatDetailsForm(forms.Form): # This gets displayed if a new Seekat is created with the option of being able to skip
    pass



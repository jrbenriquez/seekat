from django import forms
from django.core.exceptions import ValidationError
from django_countries.widgets import CountrySelectWidget


class RequestForm(forms.Form):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)


class NewSeekForm(RequestForm):
    """
    User selects or creates Seekat and Category

    Form is passed until Seek details are complete
    """
    # Seekat
    seekat_id = forms.IntegerField(required=False)
    seekat_name = forms.CharField(max_length=100, required=True)

    # Category
    category_id = forms.IntegerField(required=False)
    category_name = forms.CharField(max_length=100, required=True)

    # Seek
    seeker_id = forms.IntegerField(required=True)


    def validate_seeker_id(self, value):
        request = self.request
        if request.user and hasattr(request.user, 'seeker') and request.user.seeker.id == int(value):
            return value
        raise ValidationError('Invalid Seeker ID')


class AdditionalSeekDetailsForm(RequestForm):

    class Meta:
        widgets = {'seekat_country': CountrySelectWidget()}

    seeker_id = forms.IntegerField(required=True)
    seekat_id = forms.IntegerField(required=False)
    seekat_name = forms.CharField(required=False)
    category_id = forms.IntegerField(required=False)
    category_name = forms.CharField(required=False)

    seekat_parent_id = forms.IntegerField(required=False)
    seekat_description = forms.CharField(max_length=255, required=False)
    seekat_line1 = forms.CharField(max_length=128, required=False)
    seekat_line2 = forms.CharField(max_length=128, required=False)
    seekat_zip_code = forms.CharField(max_length=12, required=False)
    seekat_city = forms.CharField(max_length=128, required=False)
    seekat_state = forms.CharField(max_length=128, required=False)
    seekat_country = forms.CharField(max_length=2, required=False)
    category_parent_id = forms.IntegerField(required=False)
    hashtag = forms.CharField(required=False)

    def validate_seeker_id(self, value):
        request = self.request
        if request.user and hasattr(request.user, 'seeker') and request.user.seeker.id == int(value):
            return value
        raise ValidationError('Invalid Seeker ID')

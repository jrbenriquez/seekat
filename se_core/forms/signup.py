from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    password_confirm = forms.CharField()

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if not all([password, password_confirm]):
            self.add_error('password', 'Password / Password Confirmation is required')

        if password != password_confirm:
            self.add_error('password', "Passwords don't match")

        return cleaned_data


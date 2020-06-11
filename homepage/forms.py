from django import forms
from django.forms import ModelForm, PasswordInput
from django.contrib.auth.password_validation import validate_password

from user.models import User


class CreateNewUserForm(ModelForm):
    password2 = forms.CharField(label='Powtórz hasło', widget=PasswordInput())
    password = forms.CharField(label='Hasło', widget=PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password and password2:
            if password != password2:
                raise forms.ValidationError('Hasła muszą być takie same.')
            # v = validate_password()
            if error := validate_password(password=password):
                return error


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(max_length=10, widget=PasswordInput(), label='Obecne hasło')
    password1 = forms.CharField(max_length=10, widget=PasswordInput(), label='Nowe hasło')
    password2 = forms.CharField(max_length=10, widget=PasswordInput(), label='Powtórz hasło')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password and password2:
            if password != password2:
                raise forms.ValidationError('Hasła muszą być takie same.')
            if error := validate_password(password=password):
                return error

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django import forms


class SignupForm(UserCreationForm):
    # password1 = forms.CharField(
    #     label=_("Password"),
    #     strip=False,
    #     widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    #
    # )
    # password2 = forms.CharField(
    #     label=_("Password confirmation"),
    #     widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    #     strip=False,
    # )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        help_texts = {'username': None}

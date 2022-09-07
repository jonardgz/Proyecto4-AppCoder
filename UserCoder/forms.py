from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    last_name = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'last_name')
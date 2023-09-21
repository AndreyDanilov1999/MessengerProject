from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    username = forms.CharField(label="Username")

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "email",
            "password1",
            "password2",
        )

from django.contrib.auth.models import User
from django.forms import ModelForm

from django import forms

from posts.models import Post


class LoginForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class NewUserForm(ModelForm):

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')
from django import forms
from .models import Entry


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=64)
    password = forms.CharField(label='Password', max_length=64, widget=forms.PasswordInput())


class SignupForm(forms.Form):
    username = forms.CharField(label='Username', max_length=64)
    email = forms.CharField(label='Email', max_length=64, widget=forms.EmailInput())
    password = forms.CharField(widget=forms.PasswordInput())

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['prompt', 'notes', 'draft']
from django import forms
from .models import Voter


class Entryform(forms.ModelForm):
    class Meta:
        model = Voter
        exclude = ['user']




from django import forms
from .models import UrlString

class UrlStringCreateForm(forms.ModelForm):
    class Meta:
        model = UrlString
        fields = "__all__"
from django import forms
from .models import UrlData

class UrlDataCreateForm(forms.ModelForm):
    class Meta:
        model = UrlData
        fields = "__all__"
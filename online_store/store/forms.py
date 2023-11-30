from django import forms
from .models import Wear


class WearForm(forms.ModelForm):
    class Meta:
        model = Wear
        fields = ['name', 'size', 'color', 'price', 'category_id']

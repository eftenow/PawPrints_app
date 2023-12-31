from django import forms
import django
django.setup()
from paw_prints_app.pets.models import Pet


class PetCreateForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'town', 'pet_category', 'gender', 'age', 'image', 'contact_number', 'description']


class SearchForm(forms.Form):
    search = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'id': 'breedFilter', 'placeholder': "Search by breed or name.."}))


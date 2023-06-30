from django import forms

from paw_prints_app.pets.models import Pet


class PetCreateForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'pet_category', 'breed', 'age', 'image', 'description' ]


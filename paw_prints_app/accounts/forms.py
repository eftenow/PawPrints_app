from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelForm

from paw_prints_app.accounts.models import Profile
from django import forms

UserModel = get_user_model()


class CreateProfileForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ("email", "username", "password1", "password2")


class LoginProfileForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'autofocus': True,
            'placeholder': 'Username'
        })
        self.fields['password'].widget.attrs['placeholder'] = 'Password'


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'gender', 'age', 'description', 'profile_picture')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'] = forms.CharField(label='First Name', max_length=20,
                                                    initial=getattr(self.instance.profile, 'first_name'))
        self.fields['last_name'] = forms.CharField(label='Last Name', max_length=20,
                                                   initial=getattr(self.instance.profile, 'last_name'))
        self.fields['gender'] = forms.ChoiceField(label='Gender', choices=[('Male', 'Male'), ('Female', 'Female')],
                                                  initial=getattr(self.instance.profile, 'gender'))
        self.fields['age'] = forms.IntegerField(label='Age', widget=forms.NumberInput(attrs={'type': 'number'}),
                                                initial=getattr(self.instance.profile, 'age'))
        self.fields['description'] = forms.CharField(label='Description', widget=forms.Textarea,
                                                     initial=getattr(self.instance.profile, 'description'))

    def save(self, commit=True):
        profile = self.instance.profile

        profile_picture = self.cleaned_data.get('profile_picture')
        if profile_picture:
            profile.profile_picture = profile_picture

        profile.save()
        return super().save(commit=False) if commit else self.instance

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age and age < 0:
            raise forms.ValidationError("Age cannot be negative.")
        return age

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

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

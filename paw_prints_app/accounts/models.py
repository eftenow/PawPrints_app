from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core import validators
from django.db import models

from paw_prints_app.accounts.managers import PawPrintsUserManger
from paw_prints_app.accounts.validators import validate_file_size, name_contains_only_letters

from paw_prints_app.pets.models import Pet


class AppUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=20,
        validators=[validators.MinLengthValidator(2)],
        unique=True,
    )
    email = models.EmailField(
        unique=True
    )
    date_joined = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"

    objects = PawPrintsUserManger()


class Profile(models.Model):
    MAX_NAME_LEN = 20
    MIN_NAME_LEN = 2

    first_name = models.CharField(
        max_length=MAX_NAME_LEN,
        validators=[validators.MinLengthValidator(MIN_NAME_LEN), name_contains_only_letters],
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        max_length=MAX_NAME_LEN,
        validators=[validators.MinLengthValidator(MIN_NAME_LEN), name_contains_only_letters],
        null=True,
        blank=True,
    )
    age = models.PositiveIntegerField(
        null=True,
        blank=True
    )
    profile_picture = models.ImageField(upload_to='images', validators=[validate_file_size])
    description = models.TextField(
        null=True,
        blank=True
    )
    user = models.OneToOneField(to=AppUser, on_delete=models.CASCADE)

    @property
    def get_full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        elif self.first_name:
            return self.first_name
        elif self.last_name:
            return self.last_name

    @property
    def adopted_pets_count(self):
        return Pet.objects.filter(adopted_by=self.user).count()

    @property
    def pet_listings_count(self):
        return Pet.objects.filter(added_by=self.user).count()

class UserFavorites(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'pet']

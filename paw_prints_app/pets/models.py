from django.db import models
from django.template.defaultfilters import slugify
from django.conf import settings
from django.urls import reverse

UserModel = settings.AUTH_USER_MODEL


class Pet(models.Model):
    PET_CATEGORY_CHOICES = [
        ('dog', 'Dog'),
        ('cat', 'Cat'),
    ]

    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )

    name = models.CharField(max_length=30)
    pet_category = models.CharField(max_length=3, choices=PET_CATEGORY_CHOICES)
    age = models.CharField()
    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        blank=True,
        null=True,
    )
    description = models.TextField()
    image = models.ImageField(upload_to='pet_images')
    adoption_status = models.CharField(max_length=20, default='Available', blank=True)
    added_by = models.ForeignKey(UserModel, on_delete=models.CASCADE,blank=True, null=True)
    added_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    contact_number = models.IntegerField()
    slug = models.SlugField(
        unique=True,
        editable=False
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f'{self.name}-{self.id}')

        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('name_of_pet_detail_url', args=[str(self.id)])






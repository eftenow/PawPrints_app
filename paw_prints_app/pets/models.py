from django.db import models
from django.template.defaultfilters import slugify
from django.conf import settings

UserModel = settings.AUTH_USER_MODEL


class Pet(models.Model):
    PET_CATEGORY_CHOICES = [
        ('dog', 'Dog'),
        ('cat', 'Cat'),
    ]

    name = models.CharField(max_length=30)
    pet_category = models.CharField(max_length=3, choices=PET_CATEGORY_CHOICES)
    age = models.CharField()
    breed = models.ForeignKey('Breed', on_delete=models.SET_NULL, null=True, blank=True, default='Unknown')
    description = models.TextField()
    image = models.ImageField(upload_to='pet_images')
    adoption_status = models.CharField(max_length=20, default='Available', blank=True)
    added_by = models.ForeignKey(UserModel, on_delete=models.CASCADE,blank=True, null=True)
    added_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    slug = models.SlugField(
        unique=True,
        editable=False
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f'{self.name}-{self.id}')

        return super().save(*args, **kwargs)


class Breed(models.Model):
    PET_CATEGORY_CHOICES = [
        ('dog', 'Dog'),
        ('cat', 'Cat'),
    ]

    name = models.CharField(max_length=30)
    pet_category = models.CharField(max_length=3, choices=PET_CATEGORY_CHOICES)
    main_characteristics = models.CharField(blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='breed_images')
    related_pets = models.ManyToManyField('Pet', related_name='related_breeds')





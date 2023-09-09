from django.contrib import admin
from .models import Pet, Breed


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'pet_category', 'age', 'breed', 'adoption_status', 'added_by', 'adopted_by', 'added_at']
    search_fields = ['name', 'breed__name', 'added_by__username', 'adopted_by__username']
    list_filter = ['pet_category', 'adoption_status', 'breed']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    list_display = ['name', 'pet_category']
    search_fields = ['name']
    list_filter = ['pet_category']

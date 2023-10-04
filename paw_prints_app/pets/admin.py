from django.contrib import admin
from .models import Pet


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'pet_category', 'age', 'gender', 'adoption_status', 'added_by', 'added_at']
    search_fields = ['name', 'added_by__username', 'adopted_by__username']
    list_filter = ['pet_category', 'adoption_status']
    prepopulated_fields = {'slug': ('name',)}

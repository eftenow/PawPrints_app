from django.contrib import admin
from .models import AppUser, Profile, UserFavorites, Pet

@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'date_joined', 'is_staff']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'age', 'gender', 'adopted_pets_count', 'pet_listings_count']
    search_fields = ['user__username', 'first_name', 'last_name']
    list_filter = ['gender']

@admin.register(UserFavorites)
class UserFavoritesAdmin(admin.ModelAdmin):
    list_display = ['user', 'pet', 'created_at']
    search_fields = ['user__username', 'pet__name']

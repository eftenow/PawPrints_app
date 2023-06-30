from django.urls import path
from . import views
from .views import get_breeds

urlpatterns = [
    path('', views.PetListView.as_view(), name='pet_list'),
    path('create/', views.PetCreateView.as_view(), name='pet_add'),
    path('detail/<int:pk>/', views.PetDetailView.as_view(), name='pet_detail'),
    path('detail/<int:pk>/edit/', views.PetEditView.as_view(), name='pet_edit'),
    path('detail/<int:pk>/delete/', views.PetDeleteView.as_view(), name='pet_delete'),
    path('create/get_breeds/', get_breeds, name='get_breeds'),
]

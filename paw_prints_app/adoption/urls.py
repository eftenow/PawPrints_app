from django.urls import path
from . import views


urlpatterns = [
    path('apply/<int:pk>/', views.AdoptionApplicationView.as_view(), name='apply'),
    # Add more URLs specific to the adoption app as needed
]
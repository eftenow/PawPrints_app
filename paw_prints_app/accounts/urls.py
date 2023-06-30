from django.urls import path, include
from . import views


urlpatterns = [
    path('register/', views.SignUpView.as_view(), name='register'),
    path('login/', views.SignInView.as_view(), name='login'),
    path('logout/', views.SignOutView.as_view(), name='logout'),
    path('profile/<int:pk>/', include([
        path('', views.UserDetailsView.as_view(), name='account details'),
        path('edit/', views.EditUserView.as_view(), name='account edit'),
        path('delete/', views.ProfileDeleteView.as_view(), name='delete account')
    ]))
]
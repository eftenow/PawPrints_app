from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from paw_prints_app.accounts.forms import CreateProfileForm, LoginProfileForm, EditProfileForm

UserModel = get_user_model()


# Create your views here.
class SignUpView(CreateView):
    template_name = 'profile/register.html'
    form_class = CreateProfileForm

    def get_success_url(self):
        return reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = authenticate(
            self.request,
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1']
        )
        login(self.request, user)
        return response


class SignInView(LoginView):
    form_class = LoginProfileForm
    template_name = 'profile/login.html'

    success_url = reverse_lazy('home')


class SignOutView(LogoutView):
    pass


class UserDetailsView(DetailView):
    template_name = 'profile/profile-details.html'
    model = UserModel


class EditUserView(UpdateView):
    template_name = 'profile/profile-edit.html'
    model = UserModel
    form_class = EditProfileForm

    def form_valid(self, form):
        response = super().form_valid(form)
        profile = self.object.profile

        profile.first_name = form.cleaned_data['first_name']
        profile.last_name = form.cleaned_data['last_name']
        profile.gender = form.cleaned_data['gender']
        profile.age = form.cleaned_data['age']
        profile.description = form.cleaned_data['description']
        profile.profile_picture = form.cleaned_data['profile_picture']

        profile.save()
        return response

    def get_success_url(self):
        return reverse_lazy('account details', kwargs={'pk': self.object.pk})


class ProfileDeleteView(DeleteView):
    pass

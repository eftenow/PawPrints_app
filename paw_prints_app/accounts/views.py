from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from paw_prints_app.accounts.forms import CreateProfileForm, LoginProfileForm

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
    pass


class EditUserView(UpdateView):
    pass


class ProfileDeleteView(DeleteView):
    pass

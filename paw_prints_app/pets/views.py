from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from paw_prints_app.pets.forms import PetCreateForm
from paw_prints_app.pets.models import Pet, Breed


# Create your views here.
class PetListView(ListView):
    template_name = 'pet/all-pets.html'
    model = Pet


class PetCreateView(CreateView):
    template_name = 'pet/add_pet.html'
    form_class = PetCreateForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.request = self.request
        return super().form_valid(form)


class PetDetailView(DetailView):
    pass


class PetEditView(UpdateView):
    pass


class PetDeleteView(DeleteView):
    pass


def get_breeds(request):
    pet_category = request.GET.get('pet_category')
    breeds = Breed.objects.filter(pet_category=pet_category).values('id', 'name').distinct('name')
    return JsonResponse({'breeds': list(breeds)})


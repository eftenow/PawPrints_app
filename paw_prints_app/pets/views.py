from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from paw_prints_app.pets.forms import PetCreateForm, SearchForm
from paw_prints_app.pets.models import Pet, Breed


# Create your views here.
class PetListView(ListView):
    template_name = 'pet/all-pets.html'
    model = Pet

    def get_queryset(self):
        queryset = super().get_queryset()
        search_form = SearchForm(self.request.GET)

        if search_form.is_valid():
            search_text = search_form.cleaned_data['search']

            if search_text:
                queryset = queryset.filter(
                    Q(breed__name__icontains=search_text) |
                    Q(name__icontains=search_text)
                )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        search_form = SearchForm(self.request.GET)
        context['form'] = search_form
        return context



class PetCreateView(CreateView):
    template_name = 'pet/add_pet.html'
    form_class = PetCreateForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.request = self.request
        return super().form_valid(form)


class PetDetailView(DetailView):
    template_name = 'pet/pet-details.html'
    model = Pet


class PetEditView(UpdateView):
    pass


class PetDeleteView(DeleteView):
    pass


def get_breeds(request):
    pet_category = request.GET.get('pet_category')
    breeds = Breed.objects.filter(pet_category=pet_category).values('id', 'name').distinct('name')
    return JsonResponse({'breeds': list(breeds)})

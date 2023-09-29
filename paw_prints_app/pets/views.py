from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from paw_prints_app.common.models import Comment
from paw_prints_app.pets.forms import PetCreateForm, SearchForm
from paw_prints_app.pets.models import Pet, Breed

from django.core.paginator import Paginator


class PetListView(ListView):
    template_name = 'pet/all-pets.html'
    model = Pet
    context_object_name = 'object_list'
    paginate_by = 10

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
        context = super().get_context_data(**kwargs)
        search_form = SearchForm(self.request.GET)
        context['form'] = search_form
        context['object_list'] = context['page_obj']
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comment_set.all()  # Using default related_name
        return context

    def post(self, request, *args, **kwargs):
        pet = self.get_object()
        user = request.user

        comment_text = request.POST.get('content')
        Comment.objects.create(comment_text=comment_text, to_pet=pet, to_user=user)
        return redirect(pet.get_absolute_url())


class PetEditView(UpdateView):
    pass


class PetDeleteView(DeleteView):
    pass


def get_breeds(request):
    pet_category = request.GET.get('pet_category')
    breeds = Breed.objects.filter(pet_category=pet_category).values('id', 'name').distinct('name')
    return JsonResponse({'breeds': list(breeds)})

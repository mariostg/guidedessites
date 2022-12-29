from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView

from .models import Habitat, SousHabitat

class HabitatView(TemplateView):
    template_name='habitat/habitat.html'
    titre="Nos habitats"
    context={'titre':titre}

class HabitatListView(ListView):
    model=Habitat

class SousHabitatListView(ListView):
    model=SousHabitat

def index(request):
    # return HttpResponse("Page geographie")
    context = {'titre': "Bienvenue sur la page Habitat"}
    return render(request, 'habitat.html', context)


def habitat_list(request):
    habitat = Habitat.objects.all()
    return render(request, 'habitat_list.html', {'habitat': habitat})


def sous_habitat_list(request):
    sous_habitat = SousHabitat.objects.all()
    return render(request, 'sous_habitat_list.html', {'sous_habitat': sous_habitat})

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView

from .models import Habitat, SousHabitat
from .forms import HabitatForm, SousHabitatForm


def habitats(request):
    data = Habitat.objects.all()
    return render(request, "habitat/habitat-list.html", {"data": data})


def add_habitat(request):
    if request.method == "POST":
        form = HabitatForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.created_by = request.user
            form.save()
            return redirect("habitats")
    else:
        form = HabitatForm

    return render(request, "habitat/habitat_form.html", {"form": form})


def delete_habitat(request, pk):
    data = Habitat.objects.get(id=pk)
    if request.method == "POST":
        data.delete()
        return redirect("habitats")
    context = {"data": data}
    return render(request, "siteornitho/delete_template.html", context)


def update_habitat(request, pk):
    data = Habitat.objects.get(pk=pk)
    form = HabitatForm(instance=data)

    if request.method == "POST":
        form = HabitatForm(request.POST, instance=data)
        if form.is_valid():
            form = form.save(commit=False)
            form.updated_by = request.user
            form.save()
            return redirect("habitats")
    return render(request, "habitat/habitat_form.html", {"form": form, "data": data})


def sous_habitats(request):
    data = SousHabitat.objects.all()
    return render(request, "habitat/sous_habitat_list.html", {"data": data})


def add_sous_habitat(request):
    if request.method == "POST":
        form = SousHabitatForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.created_by = request.user
            form.save()
            return redirect("sous-habitats")
    else:
        form = SousHabitatForm

    return render(request, "habitat/sous_habitat_form.html", {"form": form})


def delete_sous_habitat(request, pk):
    data = SousHabitat.objects.get(id=pk)
    if request.method == "POST":
        data.delete()
        return redirect("sous-habitats")
    context = {"data": data}
    return render(request, "siteornitho/delete_template.html", context)


def update_sous_habitat(request, pk):
    data = SousHabitat.objects.get(pk=pk)
    form = SousHabitatForm(instance=data)

    if request.method == "POST":
        form = SousHabitatForm(request.POST, instance=data)
        if form.is_valid():
            form = form.save(commit=False)
            form.updated_by = request.user
            form.save()
            return redirect("sous-habitats")
    return render(request, "habitat/sous_habitat_form.html", {"form": form, "data": data})

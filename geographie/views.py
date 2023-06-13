from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Mrc, Municipalite
from .form import MrcForm, MunicipaliteForm


def mrcs(request):
    data = Mrc.objects.all()
    return render(request, "geographie/mrc-list.html", {"data": data})


def municipalites(request):
    data = Municipalite.objects.all()
    return render(request, "geographie/municipalite-list.html", {"data": data})


def delete_mrc(request, pk):
    data = Mrc.objects.get(id=pk)
    if request.method == "POST":
        data.delete()
        return redirect("mrcs")
    context = {"data": data}
    return render(request, "siteornitho/delete_template.html", context)


def delete_municipalite(request, pk):
    data = Municipalite.objects.get(id=pk)
    if request.method == "POST":
        data.delete()
        return redirect("municipalites")
    context = {"data": data}
    return render(request, "siteornitho/delete_template.html", context)


def update_mrc(request, pk):
    data = Mrc.objects.get(pk=pk)
    form = MrcForm(instance=data)

    if request.method == "POST":
        form = MrcForm(request.POST, instance=data)
        if form.is_valid():
            form = form.save(commit=False)
            form.updated_by = request.user
            form.save()
            return redirect("mrcs")
    return render(request, "geographie/mrc_form.html", {"form": form, "data": data})


def update_municipalite(request, pk):
    data = Municipalite.objects.get(pk=pk)
    form = MunicipaliteForm(instance=data)

    if request.method == "POST":
        form = MunicipaliteForm(request.POST, instance=data)
        if form.is_valid():
            form = form.save(commit=False)
            form.updated_by = request.user
            form.save()
            return redirect("municipalites")
    return render(request, "geographie/municipalite_form.html", {"form": form, "data": data})


def add_mrc(request):
    if request.method == "POST":
        form = MrcForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.created_by = request.user
            form.save()
            return redirect("mrcs")
    else:
        form = MrcForm

    return render(request, "geographie/mrc_form.html", {"form": form})


def add_municipalite(request):
    if request.method == "POST":
        form = MunicipaliteForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.created_by = request.user
            form.save()
            return redirect("municipalites")
    else:
        mrc_count = Mrc.objects.all().count()
        if mrc_count == 0:
            messages.warning(request, "Il n'est pas possible d'ajouter une municipalité car il n'existe pas de MRC")
            return redirect("municipalites")
        else:
            form = MunicipaliteForm

    return render(request, "geographie/municipalite_form.html", {"form": form})

from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib import messages
from .filters import SiteOrnithoFilter
from .models import SiteOrnitho, SiteOrnithoImage, SousHabitat
from .forms import SearchSiteForm, SiteForm, ImageForm
from . import utils


class HomeView(generic.TemplateView):
    template_name = "home.html"
    extra_context = {"is_home": True}


class SiteornithoPublishedListView(generic.ListView):
    queryset = SiteOrnitho.published.all()
    template_name = "siteornitho/siteornitho_list.html"


def catalogue(request, page=1):
    sites = SiteOrnitho.objects.all()
    form = SearchSiteForm()
    paginator = Paginator(sites, 1)

    if len(sites) == 0:
        context = {
            "sites": [],
            "m1": 0,
            "m2": 0,
            "previous_page": 0,
            "next_page": 0,
            "form": form,
        }
        messages.warning(request, "Il n'y a pas de sites dans le catalogue")
        return render(request, "siteornitho/siteornitho_detail.html", context)

    try:
        sites = paginator.page(page)
    except EmptyPage:
        # if we exceed the page limit we return the last page
        sites = paginator.page(paginator.num_pages)

    m1, m2 = utils.periode_interet(sites.object_list[0])
    next_page = page + 1
    if next_page > paginator.num_pages:
        next_page = paginator.num_pages
    previous_page = page - 1
    if previous_page < 1:
        previous_page = 1

    context = {
        "sites": sites,
        "m1": m1,
        "m2": m2,
        "previous_page": previous_page,
        "next_page": next_page,
        "form": form,
    }

    return render(request, "siteornitho/siteornitho_detail.html", context)


def sites(request):
    sites, initial = utils.search_sites(request)
    form = SearchSiteForm(initial=initial)
    context = {
        "filter": sites,
        "form": form,
        "initial": initial,
    }
    return render(request, "siteornitho/sites.html", context)


def site(request, pk):
    municipalite = ""
    nom_du_site = ""
    transport = "off"
    sous_habitat = ""
    if "municipalite" in request.GET:
        municipalite = request.GET.get("municipalite")
    if "nom_du_site" in request.GET:
        nom_du_site = request.GET.get("nom_du_site")
    if "transport" in request.GET:
        transport = request.GET.get("transport")
    if "sous_habitat" in request.GET:
        sous_habitat = request.GET.get("sous_habitat")

    initial = {
        "municipalite": municipalite,
        "nom_du_site": nom_du_site,
        "transport": transport,
        "sous_habitat": sous_habitat,
    }
    form = SearchSiteForm(initial=initial)
    sites = SiteOrnitho.objects.get(pk=pk)
    m1, m2 = utils.periode_interet(sites)
    context = {
        "sites": sites,
        "m1": m1,
        "m2": m2,
        "form": form,
    }
    return render(request, "siteornitho/site.html", context)
    # return render(request, "siteornitho/siteornitho_detail.html", context)


@login_required
def edit_site(request, pk):
    site = SiteOrnitho.objects.get(id=pk)
    form = SiteForm(instance=site)

    if request.method == "POST":
        form = SiteForm(request.POST, instance=site)
        if form.is_valid():
            form.save()
            return redirect("sites")
    return render(request, "siteornitho/site_form.html", {"form": form, "site": site})


@login_required
# @login_required(login_url="/guidedessites/users/login/")
def add_site(request):
    print(f"ULR {settings.LOGIN_URL}")
    if request.method == "POST":
        form = SiteForm(request.POST)
        if form.is_valid():
            site = form.save()
            return redirect("site", site.id)
            # return redirect("sites")
    else:
        counts = SousHabitat.objects.all().count()
        if counts == 0:
            messages.warning(
                request,
                "Il n'est pas possible d'ajouter un site sans sous-habitat définis.  Veuillez definir au moins un sous-habitat",
            )
            return redirect("sous-habitats")
        form = SiteForm

    return render(request, "siteornitho/site_form.html", {"form": form})


def delete_site(request, pk):
    site = SiteOrnitho.objects.get(id=pk)
    if request.method == "POST":
        site.delete()
        return redirect("sites")
    context = {"object": site}
    return render(request, "siteornitho/delete_template.html", context)


def images(request):
    qs = SiteOrnithoImage.objects.all()
    for im in qs:
        size = im.get_size()
        im.width = size["width"]
        im.height = size["height"]
    return render(request, "siteornitho/images.html", {"images": qs})


def add_image(request):
    print("Entering function")
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            print("Image form is valid")
            image = form.save()
            img_obj = form.instance
            return render(
                request,
                "siteornitho/image_form.html",
                {
                    "form": form,
                    "img_obj": img_obj,
                },
            )
        else:
            print("Image not valid")
    else:
        print("MEthod is not posr")
        form = ImageForm
        return render(
            request,
            "siteornitho/image_form.html",
            {
                "form": form,
            },
        )


def update_image(request, pk):
    qs = SiteOrnithoImage.objects.get(id=pk)
    form = ImageForm(instance=qs)

    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES, instance=qs)
        if form.is_valid():
            form.save()
            return redirect("images")
    return render(request, "siteornitho/image_form.html", {"form": form})


def delete_image(request, pk):
    qs = SiteOrnithoImage.objects.get(id=pk)
    if request.method == "POST":
        qs.delete()
        return redirect("images")
    context = {"object": qs}
    return render(request, "siteornitho/delete_template.html", context)

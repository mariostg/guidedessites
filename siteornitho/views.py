from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage

from django.views import generic
from django.contrib import messages
from .filters import SiteOrnithoFilter
from .models import SiteOrnitho
from .forms import SearchSiteForm
from . import utils


class HomeView(generic.TemplateView):
    template_name = "home.html"


class SiteornithoPublishedListView(generic.ListView):
    queryset = SiteOrnitho.published.all()
    template_name = "siteornitho/siteornitho_list.html"


def catalogue(request, page=1):
    sites = SiteOrnitho.objects.all()
    form = SearchSiteForm()
    paginator = Paginator(sites, 1)

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

    sites, municipalite = utils.search_sites(request)
    form = SearchSiteForm(initial={"municipalite": municipalite})
    context = {"filter": sites, "form": form, "municipalite": municipalite}
    return render(request, "siteornitho/sites.html", context)


def site(request, pk):
    municipalite = ""
    if request.GET["municipalite"]:
        municipalite = request.GET.get("municipalite")

    form = SearchSiteForm(initial={"municipalite": municipalite})
    sites = SiteOrnitho.objects.get(pk=pk)
    m1, m2 = utils.periode_interet(sites)
    context = {
        "sites": sites,
        "m1": m1,
        "m2": m2,
        "form": form,
    }
    return render(request, "siteornitho/site.html", context)

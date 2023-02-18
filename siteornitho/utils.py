from django.db.models import Q
from .models import SiteOrnitho


def periode_interet(site):
    mois = SiteOrnitho.Mois.choices
    m2 = ""
    m1 = mois[site.periode_interet_debut][1]
    if m1 != "Toute l'année":
        m2 = " à " + mois[site.periode_interet_fin][1]

    return m1, m2


def search_sites(request):

    municipalite = None
    nom_du_site = ""
    transport = "off"
    sous_habitat = ""
    sites = SiteOrnitho.objects.all()
    if request.GET.get("municipalite"):
        municipalite = request.GET.get("municipalite")
        sites = sites.filter(
            municipalite__exact=municipalite,
        )
    if request.GET.get("nom_du_site"):
        nom_du_site = request.GET.get("nom_du_site")
        sites = sites.filter(
            nom_du_site__icontains=nom_du_site,
        )
    if request.GET.get("sous_habitat"):
        sous_habitat = request.GET.getlist("sous_habitat")
        qobj = Q(sous_habitat=sous_habitat.pop())
        for sh in sous_habitat:
            qobj = qobj | Q(sous_habitat=sh)
        print(qobj)
        sites = sites.filter(qobj)
    if request.GET.get("transport"):
        sites = sites.filter(
            transport=True,
        )
    else:
        transport = False

    search_criterion = {
        "municipalite": municipalite,
        "nom_du_site": nom_du_site,
        "transport": transport,
        "sous_habitat": sous_habitat,
    }
    print(search_criterion)
    return sites, search_criterion

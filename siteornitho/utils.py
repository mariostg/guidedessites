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
    if request.GET.get("municipalite"):
        municipalite = request.GET.get("municipalite")
    sites = SiteOrnitho.objects.filter(municipalite=municipalite)
    return sites, municipalite

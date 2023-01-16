import django_filters
from .models import SiteOrnitho


class SiteOrnithoFilter(django_filters.FilterSet):
    nom_du_site = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = SiteOrnitho
        fields = ["municipalite", "periode_interet_debut", "sous_habitat", "transport"]

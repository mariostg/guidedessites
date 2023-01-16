from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.views import generic
from django.contrib import messages
from .filters import SiteOrnithoFilter
from .models import SiteOrnitho


class HomeView(generic.TemplateView):
    template_name = "home.html"


class SiteornithoListView(generic.ListView):
    model = SiteOrnitho


class SiteornithoPublishedListView(generic.ListView):
    queryset = SiteOrnitho.published.all()
    template_name = "siteornitho/siteornitho_list.html"


class SiteOrnithoPaginate(generic.ListView):
    paginate_by = 1
    model = SiteOrnitho
    context_object_name = "site"
    template_name = "siteornitho/siteornitho_detail.html"


class DetailListView(generic.ListView):
    template_name = "siteornitho/siteornitho_detail.html"
    context_object_name = "site"

    def get_queryset(self):
        data = SiteOrnitho.objects.filter(pk=self.kwargs["pk"], status=1)

        if data.exists() == False:
            messages.add_message(self.request, messages.INFO, "Aucune fiche trouvée")

        return data


def search(request):
    data = SiteOrnitho.objects.all()
    filtered = SiteOrnithoFilter(request.GET, queryset=data)
    return render(request, "siteornitho/siteornitho_filter.html", {"filter": filtered})


# class FilterView(generic.ListView):
#     model = SiteOrnitho

#     def get_queryset(self):
#         qs = self.model.objects.all()
#         filtered_list = SiteOrnithoFilter(self.request.GET, queryset=qs)
#         return filtered_list.qs


"""
from siteornitho.models import SiteOrnitho
from django.core.paginator import Paginator
site=SiteOrnitho.objects.all().select_related()
paginator=Paginator(site,1)
pobj=paginator.get_page(2)
pobj[0]
pobj[0].description_generale
"""

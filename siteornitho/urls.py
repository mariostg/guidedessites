from django.urls import path
from .views import (
    HomeView,
    SiteOrnithoPaginate,
    DetailListView,
    SiteornithoPublishedListView,
    # FilterView,
)
from . import views

# app_name = "siteornitho"
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("site/liste/", SiteornithoPublishedListView.as_view(), name="detail_list"),
    path("site/catalogue/", SiteOrnithoPaginate.as_view(), name="catalogue"),
    path("site/liste/<int:pk>/", DetailListView.as_view(), name="detail_site"),
    # path("site/filtre/", FilterView.as_view(), name="filtre_site"),
    path("site/search/", views.search, name="filtre_site"),
]

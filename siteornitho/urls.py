from django.urls import path
from . import views

# app_name = "siteornitho"
urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("sites/catalogue/", views.catalogue, name="catalogue"),
    path("sites/catalogue/<int:page>/", views.catalogue, name="catalogue"),
    path("sites/<int:pk>/", views.site, name="site"),
    path("sites/", views.sites, name="sites"),
    path(
        "site/liste/", views.SiteornithoPublishedListView.as_view(), name="detail_list"
    ),
]

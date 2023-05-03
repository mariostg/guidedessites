from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("sites/catalogue/", views.catalogue, name="catalogue"),
    path("sites/catalogue/<int:page>/", views.catalogue, name="catalogue"),
    path("sites/<int:pk>/", views.site, name="site"),
    path("sites/", views.sites, name="sites"),
    path("site/liste/", views.SiteornithoPublishedListView.as_view(), name="detail_list"),
    path("site/<int:pk>/edit/", views.edit_site, name="edit-site"),
    path("site/<int:pk>/delete/", views.delete_site, name="delete-site"),
    path("site/add/", views.add_site, name="add-site"),
    path("images/", views.images, name="images"),
    path("image/add", views.add_photo, name="add-photo"),
]

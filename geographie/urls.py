from django.urls import path
from . import views

urlpatterns = [
    path("mrcs/", views.mrcs, name="mrcs"),
    path("addmrc/", views.add_mrc, name="add-mrc"),
    path("update-mrc/<int:pk>", views.update_mrc, name="update-mrc"),
    path("delete-mrc/<int:pk>", views.delete_mrc, name="delete-mrc"),
]

urlpatterns += [
    path("municipalites/", views.municipalites, name="municipalites"),
    path("addmunicipalite/", views.add_municipalite, name="add-municipalite"),
    path("update-unicipalitec/<int:pk>", views.update_municipalite, name="update-municipalite"),
    path("delete-municipalite/<int:pk>", views.delete_municipalite, name="delete-municipalite"),
]

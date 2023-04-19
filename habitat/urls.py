from django.urls import path
from . import views

urlpatterns = [
    path("habitats/", views.habitats, name="habitats"),
    path("sous-habitats/", views.sous_habitats, name="sous-habitats"),
]

urlpatterns += [
    path("add-habitat/", views.add_habitat, name="add-habitat"),
    path("update-habitat/<int:pk>", views.update_habitat, name="update-habitat"),
    path("delete-habitat/<int:pk>", views.delete_habitat, name="delete-habitat"),
]

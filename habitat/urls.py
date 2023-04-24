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

urlpatterns += [
    path("add-sous-habitat/", views.add_sous_habitat, name="add-sous-habitat"),
    path("update-sous-habitat/<int:pk>", views.update_sous_habitat, name="update-sous-habitat"),
    path("delete-sous-habitat/<int:pk>", views.delete_sous_habitat, name="delete-sous-habitat"),
]

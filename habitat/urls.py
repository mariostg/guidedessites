from django.urls import path
from .views import HabitatView, HabitatListView,SousHabitatListView 

urlpatterns = [
    path('', HabitatView.as_view()),
    path('liste/', HabitatListView.as_view(), name='habitat-liste'),
    path('listesoushabitat/', SousHabitatListView.as_view(),name='sous-habitat-liste'),
]

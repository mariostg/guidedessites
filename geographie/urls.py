from django.urls import path
from .views import MrcListView, MunicipaliteListView

urlpatterns = [
    path('listemrc/',MrcListView.as_view() , name='mrc-liste'),
    path('listemunicipalite/',MunicipaliteListView.as_view() , name='municipalite-liste'),
]
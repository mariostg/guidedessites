from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.views.generic import ListView
from .models import Mrc, Municipalite

class MrcListView(ListView):
    model=Mrc

class MunicipaliteListView(ListView):
    model=Municipalite
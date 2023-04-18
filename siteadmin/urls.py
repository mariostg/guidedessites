from django.urls import path
from . import views

urlpatterns = [
    path("", views.siteadmin, name="site-admin"),
]

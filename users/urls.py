from django.urls import path
from . import views

urlpatterns = [
    path("", views.profiles, name="profiles"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("logout/", views.user_logout, name="logout"),
    path("account/", views.user_account, name="account"),
    path("profile/<str:pk>/", views.user_profile, name="user-profile"),
    path("edit-account/", views.edit_account, name="edit-account"),
]

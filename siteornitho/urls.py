from django.urls import path
from .views import HomeView, SiteornithoListView,DetailListView, SiteornithoPublishedListView
from . import views
# app_name = "siteornitho"
urlpatterns = [
    path('', HomeView.as_view() , name='home'),
    path('site/liste/', SiteornithoPublishedListView.as_view() ),
    path('site/liste/<int:pk>/', DetailListView.as_view(), name='detail_list'),
]
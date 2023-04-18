from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("guidedessites/users/", include("users.urls")),
    path("guidedessites/", include("siteornitho.urls")),
    path("guidedessites/habitat/", include("habitat.urls")),
    path("guidedessites/soushabitat/", include("habitat.urls")),
    path("guidedessites/geographie/", include("geographie.urls")),
    # path('__debug__/', include('debug_toolbar.urls')),
]
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = "Guide des sites - Administration"

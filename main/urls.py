from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("siteadmin/", include("siteadmin.urls")),
    path("users/", include("users.urls")),
    path("", include("siteornitho.urls")),
    path("habitat/", include("habitat.urls")),
    path("soushabitat/", include("habitat.urls")),
    path("geographie/", include("geographie.urls")),
    # path('__debug__/', include('debug_toolbar.urls')),
]
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = "Guide des sites - Administration"

"""ji_sponsorship URL Configuration
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from ji_sponsorship import settings

from sponsorship.views import index

urlpatterns = [
    path('', index, name="index"),
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

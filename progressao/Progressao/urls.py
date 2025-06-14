from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('paginas.urls')),
    path('',include('cadastros.urls')),
    path('',include('usuarios.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('paginas.urls')),
    path('',include('cadastros.urls')),
    path('',include('usuarios.urls')),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    
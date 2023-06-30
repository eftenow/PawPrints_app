from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('paw_prints_app.common.urls')),
    path('accounts/', include('paw_prints_app.accounts.urls')),
    path('pets/', include('paw_prints_app.pets.urls')),
    path('adoption/', include('paw_prints_app.adoption.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

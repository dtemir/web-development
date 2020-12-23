from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('greeting.urls')),
    path('blog/', include('blog.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/', include('authorization.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'greeting.views.error_404_view'
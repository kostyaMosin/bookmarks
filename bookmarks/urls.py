from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^account/', include('account.urls')),
    re_path(r'^social-auth/', include('social_django.urls', namespace='social')),
    re_path(r'^images/', include(('images.urls', 'images'), namespace='images')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

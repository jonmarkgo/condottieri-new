from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('machiavelli.urls')),
    path('accounts/', include('allauth.urls')),
    path('notifications/', include('notifications.urls')),
    path('profiles/', include('condottieri_profiles.urls')),
    path('avatar/', include('avatar.urls')),
    path('messages/', include('django_messages.urls')),
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
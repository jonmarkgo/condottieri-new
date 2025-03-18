from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('', include('machiavelli.urls', namespace='machiavelli')),  # This includes the summary view as '/'
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('notifications/', include('notifications.urls')),
    path('profiles/', include('condottieri_profiles.urls', namespace='profiles')),
    path('avatar/', include('avatar.urls')),
    path('messages/', include('django_messages.urls')),  # Base messaging system
    path('messages/', include('condottieri_messages.urls')),  # Extended messaging features
    path('scenarios/', include('condottieri_scenarios.urls', namespace='scenarios')),  # Scenarios app
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns 
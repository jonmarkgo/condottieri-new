"""
URL configuration for Condottieri project.
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Authentication
    path('accounts/', include('allauth.urls')),
    
    # Third-party apps
    path('notifications/', include('notifications.urls', namespace='notifications')),
    path('markdownx/', include('markdownx.urls')),
    
    # Local apps
    path('', include('machiavelli.urls')),
    path('profiles/', include('condottieri_profiles.urls')),
    path('messages/', include('condottieri_messages.urls')),
    path('events/', include('condottieri_events.urls')),
    path('scenarios/', include('condottieri_scenarios.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [
            path("__debug__/", include(debug_toolbar.urls)),
        ] + urlpatterns

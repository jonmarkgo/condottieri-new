from django.conf import settings

def settings_processor(request):
    return {
        'ACCOUNT_OPEN_SIGNUP': getattr(settings, 'ACCOUNT_OPEN_SIGNUP', False),
        'INCLUDE_GOOGLE_ANALYTICS': getattr(settings, 'INCLUDE_GOOGLE_ANALYTICS', False),
    } 
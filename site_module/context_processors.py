from .models import SiteSettings


def site_settings(request):
    """
    Context processor to make site settings available globally in templates
    """
    try:
        site_settings = SiteSettings.objects.filter(is_main_settings=True).first()
        return {
            'site_settings': site_settings
        }
    except Exception:
        # Return empty dict if there's any error (e.g., during migrations)
        return {
            'site_settings': None
        }

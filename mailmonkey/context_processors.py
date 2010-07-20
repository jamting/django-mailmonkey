"""Context Processors for mailmonkey"""
from mailmonkey.settings import MEDIA_URL

def media(request):
    """Adds media-related context variables to the context"""
    return {'NEWSLETTER_MEDIA_URL': MEDIA_URL}

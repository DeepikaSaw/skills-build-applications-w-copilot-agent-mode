# views.py for the OctoFit Tracker project

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def api_root(request):
    from django.conf import settings
    codespace_url = f"https://{settings.ALLOWED_HOSTS[0]}-8000.app.github.dev"
    return Response({
        'message': 'Welcome to the OctoFit Tracker API!',
        'codespace_url': codespace_url,
        'localhost_url': 'http://localhost:8000'
    })

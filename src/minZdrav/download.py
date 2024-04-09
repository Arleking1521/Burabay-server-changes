from django.http import HttpResponse
from django.conf import settings
import os

def download_file(request, file_name):
    if os.path.exists(file_name):
        with open(file_name, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename="{file_name}"'
            return response
    else:
        return HttpResponse("File not found", status=404)
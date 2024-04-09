from django.http import HttpResponse
from django.conf import settings
import os

def download_file(request, file_name):
    file_path = os.path.join('../media/', file_name)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename="{file_path}"'
            return response
    else:
        return HttpResponse("File not found", status=404)
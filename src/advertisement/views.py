from django.shortcuts import render
from .models import Ads, Files
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
# Create your views here.
def ads(request):
    ads = Ads.objects.all()
    for ad in ads:
        files = Files.objects.filter(ads_id = ad.pk)
        ad.files = files
    return render(request, 'infoPages/advertisement.html', {'ads':ads})

def download_file(request, file_id):
    file_obj = get_object_or_404(Files, pk=file_id)
    response = HttpResponse(file_obj.file, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{file_obj.name}.docx"'
    return response
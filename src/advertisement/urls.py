from django.urls import path
from . import views
from .views import download_file

urlpatterns = [
    path('', views.ads, name = 'ads'),
    path('download/<int:file_id>/', download_file, name='download_file'),
]
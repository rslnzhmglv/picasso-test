from django.urls import path
from .views import csv_upload, ReportsView

urlpatterns = [
    path('', csv_upload, name='upload'),
    path('api/v1/reports/', ReportsView.as_view())
]
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from .custom_filters import ReportFilter
from .models import ReportDocument, Report
from .forms import UploadDocumentForm
from .serializers import ReportSerializer
from scripts.csv_to_sql.main import export_csv_to_database
from rest_framework import generics


def csv_upload(request):
    if request.method == 'POST':
        form = UploadDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            document = ReportDocument.objects.last()
            export_csv_to_database(
                table_name='csv_to_db_api_report',
                fields=['crime_id', 'original_crime', 'report_date',
                        'call_date', 'offense_date', 'call_time',
                        'call_date_time', 'disposition', 'address',
                        'city', 'state', 'agency_id',
                        'address_type', 'common_location'],
                file_path=document.file.path,
                delimiter=','
            )
            count = document.delete()
            return render(request, 'csv_to_db_api/report.html', {'counter': count})
    else:
        form = UploadDocumentForm()
        return render(request, 'csv_to_db_api/base.html', {'form': form})


class ReportsView(generics.ListAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ReportFilter




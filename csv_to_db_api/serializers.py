from rest_framework.serializers import ModelSerializer
from .models import Report


class ReportSerializer(ModelSerializer):
    class Meta:
        model = Report
        fields = ['crime_id', 'original_crime', 'report_date',
                  'call_date', 'offense_date', 'call_time',
                  'call_date_time', 'disposition', 'address',
                  'city', 'state', 'agency_id',
                  'address_type', 'common_location'
                  ]
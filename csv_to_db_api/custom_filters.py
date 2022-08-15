from django_filters import rest_framework as filters
from .models import Report


class ReportFilter(filters.FilterSet):
    report_date = filters.DateTimeFromToRangeFilter()

    class Meta:
        model = Report
        fields = ['report_date']
from django.contrib import admin
from .models import Report, ReportDocument
# Register your models here.


admin.site.register(ReportDocument)


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ['report_date', 'call_date', 'call_date_time']
from django import forms
from .models import ReportDocument


class UploadDocumentForm(forms.ModelForm):
    class Meta:
        model = ReportDocument
        fields = ['file']
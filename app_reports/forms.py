from django import forms

from app_reports.models import ProblemReported, Report


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = "__all__"


class ProblemReportedForm(forms.ModelForm):
    class Meta:
        model = ProblemReported
        fields = "__all__"

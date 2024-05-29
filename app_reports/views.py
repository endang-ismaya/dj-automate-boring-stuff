from django.shortcuts import render

from app_reports.forms import ProblemReportedForm, ReportForm


def report_view(request):
    """Report View"""

    form = ReportForm()
    pform = ProblemReportedForm()

    context = {
        "form": form,
        "pform": pform,
    }

    return render(request, "app_reports/report.html", context)

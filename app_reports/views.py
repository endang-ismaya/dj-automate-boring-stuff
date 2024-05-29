from django.shortcuts import render

# Create your views here.

def index(request):
    """app_reports index view"""
    context = {}
    return render(request, "app_reports/index.html", context)

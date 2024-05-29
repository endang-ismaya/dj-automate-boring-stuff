from django.shortcuts import render

# Create your views here.

def index(request):
    """app_areas index view"""
    context = {}
    return render(request, "app_areas/index.html", context)

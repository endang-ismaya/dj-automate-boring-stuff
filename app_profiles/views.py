from django.shortcuts import render

# Create your views here.

def index(request):
    """app_profiles index view"""
    context = {}
    return render(request, "app_profiles/index.html", context)

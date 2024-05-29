from django.shortcuts import render

# Create your views here.

def index(request):
    """app_products index view"""
    context = {}
    return render(request, "app_products/index.html", context)

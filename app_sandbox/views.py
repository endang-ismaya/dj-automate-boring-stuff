import logging

from django.shortcuts import render

djlog = logging.getLogger("djlog")  # Get logger based on the module name
tracklog = logging.getLogger("tracklog")


def index(request):
    """app_sandbox index view"""
    djlog.info("Processing a request in sandbox:index view")
    djlog.warning("sample of warning in sandbox:index view")
    context = {}
    return render(request, "app_sandbox/index.html", context)


def app_tracker(request):
    """App tracker log test"""
    tracklog.info("User is using tracker log.")
    context = {}
    return render(request, "app_sandbox/app_tracker.html", context)

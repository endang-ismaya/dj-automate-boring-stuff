import logging

from django.shortcuts import render

djlog = logging.getLogger("djlog")  # Get logger based on the module name


def index(request):
    """app_sandbox index view"""
    djlog.info("Processing a request in sandbox:index view")
    djlog.warning("sample of warning in sandbox:index view")
    context = {}
    return render(request, "app_sandbox/index.html", context)

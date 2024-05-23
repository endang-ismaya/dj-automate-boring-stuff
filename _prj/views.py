import time

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect

from app_dataentries.tasks import celery_test_task


def celery_test(request):
    """Testing the celery"""

    # a time consuming task in seconds
    celery_test_task.delay()
    messages.success(request, "Your Test have been implemented in the background.")
    return redirect("dataentries:index")
import time

from django.http import HttpResponse

from app_dataentries.tasks import celery_test_task


def celery_test(request):
    """Testing the celery"""

    # a time consuming task in seconds
    celery_test_task.delay()

    return HttpResponse("Function executed successfully")
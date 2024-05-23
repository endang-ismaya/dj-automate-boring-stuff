# Create your views here.
from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect, render

# from app_dataentries.tasks import import_data_task
from app_dataentries.tasks import export_data_task, import_data_task
from app_dataentries.utils import check_csv_errors, get_all_custom_models
from app_uploads.models import Upload


def index(request):
    context = {}
    return render(request, "app_dataentries/index.html", context)


def import_data(request):
    """Import data"""
    if request.method == "POST":
        file_path = request.FILES.get("file_path")
        model_name = request.POST.get("model_name")

        # store this file inside the Upload model
        upload = Upload.objects.create(file=file_path, model_name=model_name)

        # # construct the full path
        relative_path = str(upload.file.url)
        base_url = str(settings.BASE_DIR)
        file_path = base_url + relative_path

        # check for the csv errors
        try:
            check_csv_errors(file_path, model_name)
        except Exception as e:
            messages.error(request, str(e))
            return redirect("dataentries:import_data")

        # handle the import data task here
        import_data_task.delay(file_path, model_name)

        # show the message to the user
        messages.success(
            request,
            "Your data is being imported, you will be notified once it is done.",
        )
        return redirect("dataentries:import_data")
    else:
        custom_models = get_all_custom_models()
        context = {
            "custom_models": custom_models,
        }
    return render(request, "app_dataentries/import_data.html", context)


def export_data(request):
    if request.method == "POST":
        model_name = request.POST.get("model_name")

        # call the export data task
        export_data_task.delay(model_name)

        # show the message to the user
        messages.success(
            request,
            "Your data is being exported, you will be notified once it is done.",
        )
        return redirect("dataentries:export_data")
    else:
        custom_models = get_all_custom_models()
        context = {
            "custom_models": custom_models,
        }
    return render(request, "app_dataentries/export_data.html", context)

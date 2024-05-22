from django.urls import path

from app_dataentries import views

app_name = "dataentries"

urlpatterns = [
    path("", views.index, name="index"),
    path("import-data", views.import_data, name="import_data"),
]

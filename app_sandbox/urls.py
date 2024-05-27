from django.urls import path

from app_sandbox import views

app_name = "sandbox"

urlpatterns = [
    path("", views.index, name="index"),
    path("app-tracker/", views.app_tracker, name="app_tracker"),
]

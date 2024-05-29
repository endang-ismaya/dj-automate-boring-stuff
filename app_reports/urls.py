from django.urls import path


from app_reports import views

app_name = "reports"

urlpatterns = [
    path("", views.index, name="index"),
]

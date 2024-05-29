from django.urls import path


from app_profiles import views

app_name = "profiles"

urlpatterns = [
    path("", views.index, name="index"),
]

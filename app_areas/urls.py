from django.urls import path


from app_areas import views

app_name = "areas"

urlpatterns = [
    path("", views.index, name="index"),
]

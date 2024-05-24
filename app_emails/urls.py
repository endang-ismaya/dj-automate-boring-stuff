from django.urls import path

from app_emails import views

app_name = "emails"

urlpatterns = [
    path("send-email/", views.send_email, name="send_email"),
    path("<int:email_id>/view", views.view_email, name="view_email"),
]

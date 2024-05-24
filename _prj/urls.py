from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("dataentries/", include("app_dataentries.urls")),
    path("celery-test", views.celery_test, name="celery_test"),
    path("", views.index, name="index"),
    # Registration & Login urls
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    # app emails
    path("emails/", include("app_emails.urls")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
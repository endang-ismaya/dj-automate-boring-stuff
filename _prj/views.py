from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

from _prj.forms import RegistrationForm
from _prj.helper import is_post
from app_dataentries.tasks import celery_test_task


def index(request):
    context = {}
    return render(request, "app_dataentries/index.html", context)

def celery_test(request):
    """Testing the celery"""

    # a time consuming task in seconds
    celery_test_task.delay()
    messages.success(request, "Your Test have been implemented in the background.")
    return redirect("dataentries:index")


def login(request):
    """User Login View"""
    if is_post(request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('index')  # Redirect to wherever you want
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout(request):
    auth_logout(request)
    return redirect('login')  # Redirect to login page after logout

def register(request):
    """User Registration View"""
    if is_post(request):
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Registration Successful")
            return redirect("login")
    else:
        form = RegistrationForm()        

    context= {"form": form}
    return render(request, "registration.html", context)
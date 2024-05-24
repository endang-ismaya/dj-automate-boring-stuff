from django.shortcuts import render


def send_email(request):
    """Sending Email View"""
    context = {}
    return render(request, "app_emails/send-email.html", context)

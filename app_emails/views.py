from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from _prj.helper import get_subslist, is_post
from app_emails.forms import EmailForm
from app_emails.models import Email
from app_emails.tasks import send_email_task


def view_email(request, email_id):
    email = get_object_or_404(Email, pk=email_id)

    context = {"email": email}
    return render(request, "app_emails/email-view.html", context)


def send_email(request):
    """Sending Email View"""
    if is_post(request):
        email_form = EmailForm(request.POST, request.FILES)

        if email_form.is_valid():
            mail_form = email_form.save()

            # send an email
            mail_subject = email_form.cleaned_data["subject"]
            message = email_form.cleaned_data["body"]
            email_list = email_form.cleaned_data["email_list"]

            # Extract email addresses from Subscriber Model
            to_email = get_subslist(email_list)

            if len(to_email) < 1:
                messages.error(
                    request,
                    f"{email_list} There is currently no email list for this group. Please create one before continuing.",
                )
                return redirect("emails:send_email")

            # check attachment
            attachment = None
            if mail_form.attachment:
                attachment = mail_form.attachment.path

            # sending email with celery
            send_email_task.delay(
                mail_subject=mail_subject,
                message=message,
                to_email=to_email,
                attachment=attachment,
            )

            # send success message
            messages.success(
                request, "The email has been sent. Please check your inbox shortly."
            )
            return redirect("emails:send_email")

    else:
        email_form = EmailForm()

    context = {"email_form": email_form}
    return render(request, "app_emails/send-email.html", context)

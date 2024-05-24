from django.contrib import messages
from django.shortcuts import redirect, render

from _prj.helper import get_subslist, is_post
from app_dataentries.utils import send_email_notification
from app_emails.forms import EmailForm


def send_email(request):
    """Sending Email View"""
    if is_post(request):
        email_form = EmailForm(request.POST, request.FILES)

        if email_form.is_valid():
            # email_form.save()

            # send an email
            mail_subject = email_form.cleaned_data["subject"]
            message = email_form.cleaned_data["body"]
            email_list = email_form.cleaned_data["email_list"]

            # Extract email addresses from Subscriber Model
            to_email, s_mails = get_subslist(email_list)

            if len(to_email) < 1:
                messages.error(
                    request,
                    f"{email_list} There is currently no email list for this group. Please create one before continuing.",
                )
                return redirect("emails:send_email")

            send_email_notification(
                mail_subject=mail_subject,
                message=message,
                to_email=s_mails,
            )

            # send success message
            messages.success(request, "Email send successfully")
            return redirect("emails:send_email")

    else:
        email_form = EmailForm()

    context = {"email_form": email_form}
    return render(request, "app_emails/send-email.html", context)

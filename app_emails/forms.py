from django import forms

from app_emails.models import Email


class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = "__all__"
        labels = {
            "email_list": "Subscription Category",
        }

from ckeditor.fields import RichTextField
from django.db import models


class SubscriptionCategory(models.Model):
    email_list = models.CharField(max_length=50)
    # creating date
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Subscription categories"
        ordering = ["email_list"]

    def __str__(self) -> str:
        return self.email_list


class Subscriber(models.Model):
    email = models.EmailField(max_length=50)
    email_list = models.ForeignKey(
        SubscriptionCategory, on_delete=models.CASCADE, related_name="subscriber"
    )
    # creating date
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.email}__{self.email_list}"


class Email(models.Model):
    subject = models.CharField(max_length=150)
    body = RichTextField()
    attachment = models.FileField(upload_to="email_attachments/", null=True, blank=True)
    sent_at = models.DateTimeField(auto_now_add=True)
    email_list = models.ForeignKey(
        SubscriptionCategory, on_delete=models.CASCADE, related_name="email"
    )
    # creating date
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.subject

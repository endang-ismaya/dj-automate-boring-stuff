from django.contrib import admin

from app_emails.models import Email, Subscriber, SubscriptionCategory


class SubscriptionCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "email_list",
        "created_at",
        "updated_at",
    )


admin.site.register(SubscriptionCategory, SubscriptionCategoryAdmin)
admin.site.register(Subscriber)
admin.site.register(Email)

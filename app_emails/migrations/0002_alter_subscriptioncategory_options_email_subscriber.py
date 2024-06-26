# Generated by Django 5.0.6 on 2024-05-24 02:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_emails", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="subscriptioncategory",
            options={
                "ordering": ["email_list"],
                "verbose_name_plural": "Subscription categories",
            },
        ),
        migrations.CreateModel(
            name="Email",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("subject", models.CharField(max_length=150)),
                ("body", models.TextField(max_length=500)),
                ("attachment", models.FileField(upload_to="email_attachments/")),
                ("sent_at", models.DateTimeField(auto_now_add=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "email_list",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="email",
                        to="app_emails.subscriptioncategory",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Subscriber",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.EmailField(max_length=50)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "email_list",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="subscriber",
                        to="app_emails.subscriptioncategory",
                    ),
                ),
            ],
        ),
    ]

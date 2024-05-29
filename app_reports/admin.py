from django.contrib import admin

from app_reports.models import Category, ProblemReported, Report

admin.site.register(Report)
admin.site.register(Category)
admin.site.register(ProblemReported)

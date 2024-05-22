from django.contrib import admin

from app_dataentries.models import Customer, Employee, Student

admin.site.register(Student)
admin.site.register(Customer)
admin.site.register(Employee)

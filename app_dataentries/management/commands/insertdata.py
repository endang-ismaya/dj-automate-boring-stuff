"""
Populate database using custom command
"""

from django.core.management.base import BaseCommand

from app_dataentries.models import Student


class Command(BaseCommand):
    help = "Inserting data into the database"

    def handle(self, *args, **kwargs):
        """Write the logic for hello world command"""
        self.stdout.write(self.style.SUCCESS("======================"))
        self.stdout.write("IMPORT DATA TO STUDENT DATABASE")
        self.stdout.write(self.style.SUCCESS("======================"))

        dataset = [
            {"roll_no": 1002, "name": "Sachin", "age": 21},
            {"roll_no": 1006, "name": "Michel", "age": 22},
            {"roll_no": 1004, "name": "Mike", "age": 23},
            {"roll_no": 1005, "name": "Joseph", "age": 25},
        ]

        for data in dataset:
            roll_no = data["roll_no"]
            existing_record = Student.objects.filter(roll_no=roll_no).exists()

            if not existing_record:
                Student.objects.create(
                    roll_no=data["roll_no"], name=data["name"], age=data["age"]
                )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f"Student with roll no {roll_no} already exists!"
                    )
                )
        self.stdout.write(self.style.SUCCESS("Data inserted successfully!"))

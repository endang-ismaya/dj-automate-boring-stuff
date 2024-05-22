from django.db import models


class Student(models.Model):
    roll_no = models.CharField(max_length=10)
    name = models.CharField(max_length=25)
    age = models.IntegerField()

    def __str__(self) -> str:
        return self.name

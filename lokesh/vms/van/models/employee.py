from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=500)
    address = models.CharField(max_length=500)

    @staticmethod
    def get_employees():
        employees = Employee.objects.all()
        return employees

    def __str__(self):
        return self.name

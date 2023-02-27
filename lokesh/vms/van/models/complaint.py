from django.db import models
from . import employee, area, dumping_van

class Complaint_employees(models.Model):
    employee_name = models.ForeignKey(employee.Employee, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)

    def register(self):
        self.save()

class Complaint_area(models.Model):
    area = models.ForeignKey(area.Area, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)

    def register(self):
        self.save()

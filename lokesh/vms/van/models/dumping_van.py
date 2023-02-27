from django.db import models
from . import employee, area

class DumpingVan(models.Model):
    number = models.CharField(max_length=50)
    driver = models.ForeignKey(employee.Employee, on_delete=models.CASCADE)
    area = models.ForeignKey(area.Area, on_delete=models.CASCADE)
    timing = models.CharField(max_length=10)

    @staticmethod
    def get_dumping_vans():
        vans = DumpingVan.objects.all()
        return vans

    def __str__(self):
        return self.number


from django.db import models

class Area(models.Model):
    area_name = models.CharField(max_length=500)

    @staticmethod
    def get_areas():
        areas = Area.objects.all()
        return areas

    def __str__(self):
        return self.area_name

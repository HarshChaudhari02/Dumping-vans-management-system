from django.shortcuts import render,redirect
from django.views import View
from van.models.area import Area

class area(View):
    def get(self, request):
        areas = Area.get_areas()
        return render(request, 'area.html', {'areas': areas})
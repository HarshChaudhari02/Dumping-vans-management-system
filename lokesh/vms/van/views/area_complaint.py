from django.shortcuts import render,redirect
from django.views import View
from van.models.area import Area
from van.models.complaint import Complaint_employees, Complaint_area
from django.shortcuts import get_object_or_404

class areaComplaint(View):
    def get(self, request):
        areas = Area.get_areas()
        return render(request, 'area_complaint.html', {'areas':areas})

    def post(self, request):
        area_id = request.POST.get('area')
        area = get_object_or_404(Area, id=area_id)
        desc = request.POST.get('description')
        areas = Area.get_areas()

        try:
            complaint = Complaint_area(area=area, description=desc)
            complaint.register()
            return redirect('homepage')
        except:
            return render(request, 'area_complaint.html', {'areas':areas})

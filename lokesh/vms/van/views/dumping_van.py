from django.shortcuts import render,redirect
from django.views import View
from van.models.dumping_van import DumpingVan

class Dumping_vans(View):
    def get(self, request):
        vans = DumpingVan.get_dumping_vans()
        return render(request, 'dumping_vans.html', {'vans': vans})
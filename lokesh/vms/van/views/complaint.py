from django.shortcuts import render,redirect
from django.views import View


class complaints(View):
    def get(self, request):
        return render(request, 'complaint.html')
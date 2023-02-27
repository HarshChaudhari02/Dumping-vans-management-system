from django.shortcuts import render,redirect
from django.views import View
from van.models.employee import Employee

class employee(View):
    def get(self, request):
        employees = Employee.get_employees()
        return render(request, 'employee.html', {'employees': employees})
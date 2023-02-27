from django.shortcuts import render,redirect
from django.views import View
from van.models.employee import Employee
from van.models.complaint import Complaint_employees, Complaint_area
from django.shortcuts import get_object_or_404

class employeeComplaint(View):
    def get(self, request):
        employees = Employee.get_employees()
        return render(request, 'employee_complaint.html', {'employees':employees})
    def post(self, request):
        employee_id = request.POST.get('employee')
        employee = get_object_or_404(Employee, id=employee_id)
        desc = request.POST.get('description')
        employees = Employee.get_employees()

        try:
            complaint = Complaint_employees(employee_name=employee, description=desc)
            complaint.register()
            return redirect('homepage')
        except:
            return render(request, 'employee_complaint.html', {'employees':employees})
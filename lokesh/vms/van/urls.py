from django.urls import path
from .views import home, dumping_van, area, employee, complaint, employee_complaint, area_complaint, login, signup, forgot_password

urlpatterns = [
    path('', home.index, name='homepage'),
    path('dumping_vans', dumping_van.Dumping_vans.as_view(), name='dumping_vans'),
    path('area', area.area.as_view(), name='area'),
    path('employee', employee.employee.as_view(), name='employee'),
    path('complaint', complaint.complaints.as_view(), name='complaint'),
    path('employee_complaint', employee_complaint.employeeComplaint.as_view(), name='employee_complaint'),
    path('area_complaint', area_complaint.areaComplaint.as_view(), name='area_complaint'),
    path('login', login.Login.as_view(), name='login'),
    path('logout', login.logout, name='logout'),
    path('signup', signup.Signup.as_view(), name='signup'),
    path('forgot_password', forgot_password.ForgotPassword.as_view(), name='forgot_password'),
]
from django.contrib import admin
from .models.complaint import Complaint_area, Complaint_employees
from .models.area import Area
from .models.dumping_van import DumpingVan
from .models.employee import Employee
from .models.user import User
# Register your models here.

admin.site.register(Complaint_area)
admin.site.register(Complaint_employees)
admin.site.register(Area)
admin.site.register(DumpingVan)
admin.site.register(Employee)
admin.site.register(User)


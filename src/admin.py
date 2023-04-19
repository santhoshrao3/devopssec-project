from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(teacher)
admin.site.register(student)
admin.site.register(subject)
admin.site.register(grades)
admin.site.register(timetable_management)
admin.site.register(reports)
admin.site.register(attendance)
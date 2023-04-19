from django.urls import path
from .views import *



urlpatterns = [
    
    path('', home, name='home'),
    path('logout/', logout, name='logout'),
    path('teacher-login/', teacher_login, name='teacher-login'),
    # studnts
    path('all-students', all_students, name='all-students'),
    path('add-student', add_student, name='add-student'),\
    path('update-student/<int:pk>', update_student, name='update-student'),    
    # course
    path('all-courses', all_courses, name='all-courses'),
    path('add-courses', add_course, name='add-courses'),
    path('update-course/<int:pk>', update_course, name='update-course'),

    # subject
    path('all-subjects', all_subject, name='all-subjects'),
    path('add-subjects', add_subject, name='add-subjects'),
    path('update-subject/<int:pk>', update_subject, name='update-subject'),

    # timetable_management
    path('all-timetable_management', all_timetable_management, name='all-timetable_management'),
    path('add-timetable_management', add_timetable_management, name='add-timetable_management'),
    path('update-timetable_management/<int:pk>', update_timetable_management, name='update-timetable_management'),

   # reports
    path('all-reports/<int:pk>', all_reports, name='all-reports'),
   path('add-reports/<int:pk>', add_reports, name='add-reports'),
    path('update-reports/<int:pk>', update_reports, name='update-reports'),

    # attendance
    path('all-attendances/<int:pk>', all_attendances, name='all-attendances'),
    path('add-attendance/<int:pk>', add_attendance, name='add-attendance'),
    path('update-attendance/<int:pk>', update_attendance, name='update-attendance'),

]

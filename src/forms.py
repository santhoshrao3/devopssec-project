from dataclasses import field
from django import forms
from .models import *
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.widgets import NumberInput



# class HotelForm(forms.ModelForm):
#     event_type_id = forms.ModelChoiceField(queryset=event_type.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
#     event_description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
#     check_in = forms.DateField(label="Select Check-In Date",required=True, widget=NumberInput(attrs={'type':'date' , "class": "form-control"}))   
#     event_date = forms.DateField(label="Select Event Date",required=True, widget=NumberInput(attrs={'type':'date' , "class": "form-control"}))
        
#     class Meta:
#         model = booking_hotel
#         exclude = ['user','hotel_id']


class StudentForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    dob = forms.DateField(label="DOB",required=True, widget=NumberInput(attrs={'type':'date' , "class": "form-control"}))
    course = forms.ModelChoiceField(queryset=courses.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = student
        exclude = ['teacher_id']

class CourseForm(forms.ModelForm):
    course_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = courses
        fields = '__all__'
        
class SubjectForm(forms.ModelForm):
    subject_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = subject
        fields = '__all__'        


class TimetableManagementForm(forms.ModelForm):
    subject_id = forms.ModelChoiceField(queryset=subject.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    start_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time','class': 'form-control'}))
    end_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time','class': 'form-control'}))
    day = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    date = forms.DateField(label="Select Date",required=True, widget=NumberInput(attrs={'type':'date' , "class": "form-control"}))
    class Meta:
        model = timetable_management
        exclude = ('teacher_id',)    

class ReportForm(forms.ModelForm):
    subject_id = forms.ModelChoiceField(queryset=subject.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    grade = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    date = forms.DateField(widget=NumberInput(attrs={'type':'date' , "class": "form-control"}))
    class Meta:
        model = reports
        exclude = ('teacher_id','student_id',)

GEEKS_CHOICES =(
    ("present", "present"),
    ("absent", "absent"),
  
)


class AttendanceForm(forms.ModelForm):
    date = forms.DateField(widget=NumberInput(attrs={'type':'date' , "class": "form-control"}))
    status = forms.ChoiceField(choices = GEEKS_CHOICES , widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = attendance
        exclude = ('teacher_id','student_id',)
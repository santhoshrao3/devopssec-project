from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import login, authenticate ,logout as deauth
from django.contrib.auth.decorators import login_required
# Create your views here.


def logout(request):
    deauth(request)
    messages.success(request, 'Logged Out Successfully')
    return redirect('teacher-login')

def teacher_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('teacher-login')
    return render(request, 'teacher_login.html')    


@login_required(login_url='teacher-login')
def home(request):
    return render(request, 'home.html')

@login_required(login_url='teacher-login')
def all_students(request):
    get_teacher = teacher.objects.get(user=request.user)
    get_students = student.objects.filter(teacher_id=get_teacher)
    print(get_students)
    return render(request, 'students.html', {'students': get_students})
@login_required(login_url='teacher-login')
def add_student(request):
    form = StudentForm()
    get_teacher = teacher.objects.get(user=request.user)
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            fr=form.save(commit=False)
            fr.teacher_id = get_teacher
            fr.save()
            messages.success(request, 'Student Added Successfully')
            return redirect('all-students')

    return render(request, 'add.html', {'form': form})        
@login_required(login_url='teacher-login')
def update_student(request, pk):
    get_student = student.objects.get(id=pk)
    form = StudentForm(instance=get_student)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=get_student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student Updated Successfully')
            return redirect('all-students')

    return render(request, 'add.html', {'form': form})
@login_required(login_url='teacher-login')
def all_courses(request):
    get_courses = courses.objects.all()
    return render(request, 'courses.html', {'courses': get_courses})

@login_required(login_url='teacher-login')
def add_course(request):
    form = CourseForm()
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course Added Successfully')
            return redirect('all-courses')

    return render(request, 'add.html', {'form': form})
@login_required(login_url='teacher-login')
def update_course(request, pk):
    get_course = courses.objects.get(id=pk)
    form = CourseForm(instance=get_course)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=get_course)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course Updated Successfully')
            return redirect('all-courses')

    return render(request, 'add.html', {'form': form})

@login_required(login_url='teacher-login') 
def all_subject(request):
    get_subjects = subject.objects.all()
    return render(request, 'subjects.html', {'subjects': get_subjects})
@login_required(login_url='teacher-login')
def add_subject(request):
    form = SubjectForm()
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subject Added Successfully')
            return redirect('all-subjects')

    return render(request, 'add.html', {'form': form})
@login_required(login_url='teacher-login')
def update_subject(request , pk):
    get_subject = subject.objects.get(id=pk)
    form = SubjectForm(instance=get_subject)
    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=get_subject)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subject Updated Successfully')
            return redirect('all-subjects')

    return render(request, 'add.html', {'form': form})
@login_required(login_url='teacher-login')
def all_timetable_management(request):
    get_timetable_management = timetable_management.objects.all()
    return render(request, 'tables.html', {'tables': get_timetable_management})


@login_required(login_url='teacher-login')
def add_timetable_management(request):
    form = TimetableManagementForm()
    get_teacher = teacher.objects.get(user=request.user)
    if request.method == 'POST':
        form = TimetableManagementForm(request.POST)
        if form.is_valid():
            fr=form.save(commit=False)
            fr.teacher_id = get_teacher
            fr.save()
            messages.success(request, 'Timetable Management Added Successfully')
            return redirect('all-timetable_management')

    return render(request, 'add.html', {'form': form})
@login_required(login_url='teacher-login')
def update_timetable_management(request, pk):
    get_timetable_management = timetable_management.objects.get(id=pk)
    form = TimetableManagementForm(instance=get_timetable_management)
    if request.method == 'POST':
        form = TimetableManagementForm(request.POST, instance=get_timetable_management)
        if form.is_valid():
            form.save()
            messages.success(request, 'Timetable Management Updated Successfully')
            return redirect('all-timetable_management')

    return render(request, 'add.html', {'form': form})

@login_required(login_url='teacher-login')
def all_reports(request , pk):
    get_teacher = teacher.objects.get(user=request.user)
    get_student = student.objects.get(id=pk)
    get_reports = reports.objects.filter(student_id=get_student , teacher_id=get_teacher)
    context ={
        'reports': get_reports ,
        'student': get_student
     
     }
    return render(request, 'reports.html',context)

@login_required(login_url='teacher-login')
def add_reports(request , pk):
    get_teacher = teacher.objects.get(user=request.user)
    get_student = student.objects.get(id=pk)
    form = ReportForm()
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            fr=form.save(commit=False)
            fr.student_id = get_student
            fr.teacher_id = get_teacher
            fr.save()
            messages.success(request, 'Report Added Successfully')
            return redirect('all-reports', pk)

    return render(request, 'add.html', {'form': form})
@login_required(login_url='teacher-login')
def update_reports(request, pk):
    get_reports = reports.objects.get(id=pk)
    form = ReportForm(instance=get_reports)
    if request.method == 'POST':
        form = ReportForm(request.POST, instance=get_reports)
        if form.is_valid():
            form.save()
            messages.success(request, 'Report Updated Successfully')
            return redirect('all-reports', get_reports.student_id.id)

    return render(request, 'add.html', {'form': form})

@login_required(login_url='teacher-login')
def all_attendances(request , pk):
    get_student = student.objects.get(id=pk)
    get_attendances = attendance.objects.filter(student_id=get_student)
    context ={

        'attendances': get_attendances,
        'student': get_student
     
     }
    return render(request, 'attendances.html',context) 


@login_required(login_url='teacher-login')
def add_attendance(request,pk):
    get_teacher = teacher.objects.get(user=request.user)
    get_student = student.objects.get(id=pk)
    form = AttendanceForm()
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            fr=form.save(commit=False)
            fr.student_id = get_student
            fr.teacher_id = get_teacher
            fr.save()
            messages.success(request, 'Attendance Added Successfully')
            return redirect('all-attendances', pk)
    return render(request, 'add.html', {'form': form})

@login_required(login_url='teacher-login')
def update_attendance(request, pk):
    get_attendance = attendance.objects.get(id=pk)
    form = AttendanceForm(instance=get_attendance)
    if request.method == 'POST':
        form = AttendanceForm(request.POST, instance=get_attendance)
        if form.is_valid():
            form.save()
            messages.success(request, 'Attendance Updated Successfully')
            return redirect('all-attendances', get_attendance.student_id.id)

    return render(request, 'add.html', {'form': form})






from django.db import models

# Create your models here.
# Attendance Controls
# Keep track of your grades.
# Timetable Management
# Reports to Create
# System for logging in and out

class teacher(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username

class courses(models.Model):
    course_name = models.CharField(max_length=100)

    def __str__(self):
        return self.course_name

class student(models.Model):
    teacher_id = models.ForeignKey(teacher , on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    dob = models.DateField()
    course = models.ForeignKey(courses , on_delete=models.CASCADE)
    #stream = models.CharField(max_length=100 ,choices=[('engineering','engineering'),('medical','medical'),('neev','neev')])    

    def __str__(self):
        return self.name

class subject(models.Model):
    subject_name = models.CharField(max_length=100)


    def __str__(self):
        return self.subject_name


class grades(models.Model):
    teacher_id = models.ForeignKey(teacher , on_delete=models.CASCADE)
    student_id = models.ForeignKey(student , on_delete=models.CASCADE)
    subject_id = models.ForeignKey(subject , on_delete=models.CASCADE)
    grade = models.CharField(max_length=10)
    date = models.DateField()

    def __str__(self):
        return self.student_id.name

class timetable_management(models.Model):
    teacher_id = models.ForeignKey(teacher , on_delete=models.CASCADE)
    subject_id = models.ForeignKey(subject , on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    day = models.CharField(max_length=10)
    date = models.DateField()

    def __str__(self):
        return self.subject_id.subject_name

class reports(models.Model):
    teacher_id = models.ForeignKey(teacher , on_delete=models.CASCADE)
    student_id = models.ForeignKey(student , on_delete=models.CASCADE)
    subject_id = models.ForeignKey(subject , on_delete=models.CASCADE)
    grade = models.CharField(max_length=10)
    date = models.DateField()

    def __str__(self):
        return self.student_id.name
class attendance(models.Model):
    teacher_id = models.ForeignKey(teacher , on_delete=models.CASCADE)
    student_id = models.ForeignKey(student , on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10 , choices=[('present','present'),('absent','absent')])
    
    def __str__(self):
        return self.student_id.name
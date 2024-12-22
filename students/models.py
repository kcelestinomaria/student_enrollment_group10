from django.db import models
from django.utils import timezone

# Create your models here.

#This is the models for school/Department the student is enrolled to Example School of computing and Engineering Sciences
class School(models.Model):
    school_name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=1)

    def __str__(self):

        return self.school_name
    

# Student Model Class
# Shows the details of the students being enrolled
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=13,default=1)
    enrollment_date = models.DateField(auto_now_add=True)
    date_of_birth = models.DateField(default=timezone.now)
    address = models.TextField(default='')
    phone_number = models.CharField(max_length=15)
    date_enrolled = models.DateTimeField(auto_now_add=True)
    program = models.ForeignKey('Program', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.program.program_name if self.program else 'No Program'}"


class Course(models.Model):
    course_code = models.CharField(max_length=20, unique=True)
    course_name = models.CharField(max_length=200)
    description = models.TextField()
    credits = models.PositiveIntegerField()
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.course_name 
    
class Department(models.Model):
    department_code = models.CharField(max_length=20, unique=True)
    department_name = models.CharField(max_length=200)
    head_of_department = models.CharField(max_length=200)

    def __str__(self):
        return self.department_name
    
# Modify Program model to improve readability in admin
class Program(models.Model):
    program_code = models.CharField(max_length=20, unique=True)
    program_name = models.CharField(max_length=200)
    department = models.ForeignKey('Department', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.program_code} - {self.program_name}"


class Enrollment(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(auto_now_add=True)
    grade = models.CharField(max_length=5, null=True, blank=True)  # Optional grade field

    def __str__(self):
        return f"{self.student} - {self.course}"

class Instructor(models.Model):
    instructor_id = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class ClassSession(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    instructor = models.ForeignKey('Instructor', on_delete=models.SET_NULL, null=True, blank=True)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)
    location = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.course} - {self.start_time}"

class Attendance(models.Model):
    class_session = models.ForeignKey('ClassSession', on_delete=models.CASCADE)
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    attendance_status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent')])

    def __str__(self):
        return f"{self.student} - {self.class_session}"

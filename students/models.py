from django.db import models
<<<<<<< HEAD
from django.utils import timezone
=======
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
>>>>>>> 8d6daf8216be6ddde3735cee99643f567af850da

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
<<<<<<< HEAD
    date_of_birth = models.DateField(default=timezone.now)
    address = models.TextField(default='')
    phone_number = models.CharField(max_length=15)
    date_enrolled = models.DateTimeField(auto_now_add=True)
    program = models.ForeignKey('Program', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

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
    
class Program(models.Model):
    program_code = models.CharField(max_length=20, unique=True)
    program_name = models.CharField(max_length=200)
    department = models.ForeignKey('Department', on_delete=models.CASCADE)

    def __str__(self):
        return self.program_name

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
=======
    created_by = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=1)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Academic year of the enrollment period
class AcademicYear(models.Model):
    academic_year_name = models.CharField(max_length=255, unique=True)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=1)

    def clean(self):
        if self.start_date >= self.end_date:
            raise ValidationError("Start date must be before end date.")

    def __str__(self):
        return self.academic_year_name

# The Course the student is being enrolled to
class Course(models.Model):
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField()
    credits = models.IntegerField()
    created_by = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=1)
    school = models.ForeignKey(School, on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.title

# The semester the student is being enrolled
class Semester(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    AcademicYear = models.ForeignKey(AcademicYear, on_delete=models.CASCADE,default=1)
    created_by = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=1)

    def __str__(self):
        return self.name

# The Models for making the enrollment. Where if you are enrolled the data will be stored in the database
class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE,default=1)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField()
    AcademicYear = models.ForeignKey(AcademicYear, on_delete=models.CASCADE,default=1)
    created_by = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=1)

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name} enrolled in {self.course.title}"
>>>>>>> 8d6daf8216be6ddde3735cee99643f567af850da

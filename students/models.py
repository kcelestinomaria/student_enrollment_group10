from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

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

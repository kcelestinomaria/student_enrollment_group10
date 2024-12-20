from django import forms
from .models import School, Student, AcademicYear, Course, Semester, Enrollment

# School Form
class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['school_name']

# Student Form
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'phone_number']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Student.objects.filter(email=email).exists():
            raise forms.ValidationError("A student with this email already exists.")
        return email

# Academic Year Form
class AcademicYearForm(forms.ModelForm):
    class Meta:
        model = AcademicYear
        fields = ['academic_year_name', 'start_date', 'end_date']

# Course Form
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'code', 'description', 'credits', 'school']

# Semester Form
class SemesterForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = ['name', 'start_date', 'end_date', 'academic_year']

# Enrollment Form
class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['student', 'school', 'course', 'academic_year']

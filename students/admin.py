from django.contrib import admin
from .models import Student, AcademicYear, Course, Semester, Enrollment, School

admin.site.register(School)
admin.site.register(Student)
admin.site.register(AcademicYear)
admin.site.register(Course)
admin.site.register(Semester)
admin.site.register(Enrollment)




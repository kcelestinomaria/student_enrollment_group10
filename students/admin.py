from django.contrib import admin
from .models import Student, Program, Department

# Register your models here.

# Let's register program model with more readable information
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('program_code', 'program_name', 'department')
    search_fields = ['program_code', 'program_name']

# We'll also register the student model with an inline display of program
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'program', 'enrollment_date')
    search_fields = ['first_name', 'last_name', 'email']
    list_filter = (['program', 'first_name'])

admin.site.register(Student, StudentAdmin)
admin.site.register(Program, ProgramAdmin)
admin.site.register(Department)


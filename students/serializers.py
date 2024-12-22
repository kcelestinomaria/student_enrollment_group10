from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Student, Course, Department, Program, Enrollment, Instructor, ClassSession, Attendance

# Student Serializer
class StudentSerializer(serializers.ModelSerializer):
    # We use Slug-related field to reference the program by its name
    program = serializers.SlugRelatedField(slug_field='program_name', queryset=Program.objects.all(), required=False)
    
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'enrollment_date', 'date_of_birth', 'address', 'program']

# Course Serializer
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

# Department Serializer
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

# Program Serializer
class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = ['program_code', 'program_name']

# Enrollment Serializer
class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'

# Instructor Serializer
class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = '__all__'

# ClassSession Serializer
class ClassSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassSession
        fields = '__all__'

# Attendance Serializer
class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'

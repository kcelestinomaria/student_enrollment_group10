from django.contrib.auth.models import User
from rest_framework import serializers
<<<<<<< HEAD
from .models import Student, Course, Department, Program, Enrollment, Instructor, ClassSession, Attendance

# Student Serializer
=======
from .models import Student, AcademicYear, Course, Semester, Enrollment, School

# Serializer for the School model
class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['id', 'school_name', 'created_at', 'created_by']

# Serializer for the Student model
>>>>>>> 8d6daf8216be6ddde3735cee99643f567af850da
class StudentSerializer(serializers.ModelSerializer):
    created_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'enrollment_date', 'created_by']

<<<<<<< HEAD
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
        fields = '__all__'

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
=======
# Serializer for the AcademicYear model
class AcademicYearSerializer(serializers.ModelSerializer):
    created_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = AcademicYear
        fields = ['id', 'academic_year_name', 'start_date', 'end_date', 'created_at', 'updated_at', 'created_by']

# Serializer for the Course model
class CourseSerializer(serializers.ModelSerializer):
    created_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    school = serializers.PrimaryKeyRelatedField(queryset=School.objects.all())

    class Meta:
        model = Course
        fields = ['id', 'title', 'code', 'description', 'credits', 'created_by', 'school']

# Serializer for the Semester model
class SemesterSerializer(serializers.ModelSerializer):
    AcademicYear = serializers.PrimaryKeyRelatedField(queryset=AcademicYear.objects.all())
    created_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Semester
        fields = ['id', 'name', 'start_date', 'end_date', 'AcademicYear', 'created_by']

# Serializer for the Enrollment model
class EnrollmentSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
    school = serializers.PrimaryKeyRelatedField(queryset=School.objects.all())
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())
    AcademicYear = serializers.PrimaryKeyRelatedField(queryset=AcademicYear.objects.all())
    created_by = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Enrollment
        fields = ['id', 'student', 'school', 'course', 'enrollment_date', 'AcademicYear', 'created_by']
>>>>>>> 8d6daf8216be6ddde3735cee99643f567af850da

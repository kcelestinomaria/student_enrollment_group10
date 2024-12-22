from django.shortcuts import render
from rest_framework import generics
from .models import Student, Course, Department, Program, Enrollment, Instructor, ClassSession, Attendance
from .serializers import StudentSerializer, CourseSerializer, DepartmentSerializer, ProgramSerializer, EnrollmentSerializer, InstructorSerializer, ClassSessionSerializer, AttendanceSerializer
from django.http import JsonResponse

# Root API View
def api_root(request):
    return JsonResponse({
        "students_list_create": "/api/students/",
        "student_detail": "/api/students/<int:pk>/",
        "courses_list_create": "/api/courses/",
        "course_detail": "/api/courses/<int:pk>/",
        "departments_list_create": "/api/departments/",
        "department_detail": "/api/departments/<int:pk>/",
        "programs_list_create": "/api/programs/",
        "program_detail": "/api/programs/<int:pk>/",
        "enrollments_list_create": "/api/enrollments/",
        "enrollment_detail": "/api/enrollments/<int:pk>/",
        "instructors_list_create": "/api/instructors/",
        "instructor_detail": "/api/instructors/<int:pk>/",
        "class_sessions_list_create": "/api/class_sessions/",
        "class_session_detail": "/api/class_sessions/<int:pk>/",
        "attendance_list_create": "/api/attendance/",
        "attendance_detail": "/api/attendance/<int:pk>/",
    })

# Student Views
class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def perform_create(self, serializer):
        # Make sure we handle any special login on creation
        serializer.save()

class StudentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# Course Views
class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

# Department Views
class DepartmentListCreateView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DepartmentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

# Program Views
class ProgramListCreateView(generics.ListCreateAPIView):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer

    def perform_create(self, serializer):
        serializer.save()

class ProgramRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer

# Enrollment Views
class EnrollmentListCreateView(generics.ListCreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

class EnrollmentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

# Instructor Views
class InstructorListCreateView(generics.ListCreateAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

class InstructorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

# ClassSession Views
class ClassSessionListCreateView(generics.ListCreateAPIView):
    queryset = ClassSession.objects.all()
    serializer_class = ClassSessionSerializer

class ClassSessionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClassSession.objects.all()
    serializer_class = ClassSessionSerializer

# Attendance Views
class AttendanceListCreateView(generics.ListCreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

class AttendanceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

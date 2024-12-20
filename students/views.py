from django.shortcuts import render
from rest_framework import generics
<<<<<<< HEAD
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
=======
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.permissions import AllowAny,IsAdminUser
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication


from .models import School, Student, AcademicYear, Course, Semester, Enrollment
from .serializers import (SchoolSerializer, StudentSerializer, AcademicYearSerializer, CourseSerializer, SemesterSerializer, EnrollmentSerializer)

# Permission Class for Admin or Read-Only
from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

# Views for School
class SchoolListCreateView(generics.ListCreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class SchoolRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(created_by=self.request.user)

# Views for Student
>>>>>>> 8d6daf8216be6ddde3735cee99643f567af850da
class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class StudentRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
<<<<<<< HEAD

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
=======
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(created_by=self.request.user)

# Views for AcademicYear
class AcademicYearListCreateView(generics.ListCreateAPIView):
    queryset = AcademicYear.objects.all()
    serializer_class = AcademicYearSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class AcademicYearRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = AcademicYear.objects.all()
    serializer_class = AcademicYearSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(created_by=self.request.user)

# Views for Course
class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class CourseRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(created_by=self.request.user)

# Views for Semester
class SemesterListCreateView(generics.ListCreateAPIView):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class SemesterRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(created_by=self.request.user)

# Views for Enrollment
class EnrollmentListCreateView(generics.ListCreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class EnrollmentRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(created_by=self.request.user)



class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        # Disable CSRF check
        return

@method_decorator(csrf_exempt, name='dispatch')
class SignupView(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication,)
    permission_classes = [AllowAny]
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if username and password:
            if User.objects.filter(username=username).exists():
                return Response({"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)
            user = User.objects.create_user(username=username, password=password)
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response({"error": "Username and password required"}, status=status.HTTP_400_BAD_REQUEST)
>>>>>>> 8d6daf8216be6ddde3735cee99643f567af850da

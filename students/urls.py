from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_root),
    
    # Student URLs
    path('students/', views.StudentListCreateView.as_view(), name='student-list-create'),
    path('students/<int:pk>/', views.StudentRetrieveUpdateDestroyView.as_view(), name='student-detail'),  # Change to pk
    
    # Course URLs
    path('courses/', views.CourseListCreateView.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', views.CourseRetrieveUpdateDestroyView.as_view(), name='course-detail'),  # Change to pk
    
    # Department URLs
    path('departments/', views.DepartmentListCreateView.as_view(), name='department-list-create'),
    path('departments/<int:pk>/', views.DepartmentRetrieveUpdateDestroyView.as_view(), name='department-detail'),  # Change to pk
    
    # Program URLs
    path('programs/', views.ProgramListCreateView.as_view(), name='program-list-create'),
    path('programs/<int:pk>/', views.ProgramRetrieveUpdateDestroyView.as_view(), name='program-detail'),  # Change to pk
    
    # Enrollment URLs
    path('enrollments/', views.EnrollmentListCreateView.as_view(), name='enrollment-list-create'),
    path('enrollments/<int:pk>/', views.EnrollmentRetrieveUpdateDestroyView.as_view(), name='enrollment-detail'),  # Change to pk
    
    # Instructor URLs
    path('instructors/', views.InstructorListCreateView.as_view(), name='instructor-list-create'),
    path('instructors/<int:pk>/', views.InstructorRetrieveUpdateDestroyView.as_view(), name='instructor-detail'),  # Change to pk
    
    # ClassSession URLs
    path('class_sessions/', views.ClassSessionListCreateView.as_view(), name='class-session-list-create'),
    path('class_sessions/<int:pk>/', views.ClassSessionRetrieveUpdateDestroyView.as_view(), name='class-session-detail'),  # Change to pk
    
    # Attendance URLs
    path('attendance/', views.AttendanceListCreateView.as_view(), name='attendance-list-create'),
    path('attendance/<int:pk>/', views.AttendanceRetrieveUpdateDestroyView.as_view(), name='attendance-detail'),  # Change to pk
]

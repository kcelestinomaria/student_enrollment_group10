from django.urls import path
from . import views

urlpatterns = [
    # School URLs
    path('schools/', views.SchoolListCreateView.as_view(), name='school-list-create'),
    path('schools/<int:pk>/', views.SchoolRetrieveUpdateView.as_view(), name='school-retrieve-update'),

    # Student URLs
    path('students/', views.StudentListCreateView.as_view(), name='student-list-create'),
    path('students/<int:pk>/', views.StudentRetrieveUpdateView.as_view(), name='student-retrieve-update'),

    # AcademicYear URLs
    path('academic-years/', views.AcademicYearListCreateView.as_view(), name='academic-year-list-create'),
    path('academic-years/<int:pk>/', views.AcademicYearRetrieveUpdateView.as_view(), name='academic-year-retrieve-update'),

    # Course URLs
    path('courses/', views.CourseListCreateView.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', views.CourseRetrieveUpdateView.as_view(), name='course-retrieve-update'),

    # Semester URLs
    path('semesters/', views.SemesterListCreateView.as_view(), name='semester-list-create'),
    path('semesters/<int:pk>/', views.SemesterRetrieveUpdateView.as_view(), name='semester-retrieve-update'),

    # Enrollment URLs
    path('enrollments/', views.EnrollmentListCreateView.as_view(), name='enrollment-list-create'),
    path('enrollments/<int:pk>/', views.EnrollmentRetrieveUpdateView.as_view(), name='enrollment-retrieve-update'),

    # Signup URL
    path('signup/', views.SignupView.as_view(), name='signup'),
]

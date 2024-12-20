# Student Enrollment System

## Group members
1. Amina Abigael- 100485
2. Kariuki Celestine - 116533
3. Eghosa Edokpolo - 170492
4. Wayne Opanja -166937
5. Mumo Mwangangi - 165437
6. Mohammed Mumin -

## Overview
This project is a Django-based API application that simulates a student enrollment system. 
It manages schools, students, courses, academic years, semesters, and enrollments. 
The application provides CRUD operations for all entities and enforces relationships and constraints between them.

## Features
Manage school, student, course, semester, enrolment and academic year records.
Handle student enrollments, linking students to courses and schools.
Provide RESTful API endpoints for all operations.

## System Requirements
Python 3.12+ installed on your system.
Django 5.0+ and Django Rest Framework 3.14+.

## project implemenatation and relation 

### Models
The Student Enrollment System consists of six key models:

1. School: Represents an institution/Department each student is enrolled to. 
-Relationships: A school can offer multiple courses, and students enroll in courses through their respective schools.
-Fields:
school_name (unique)
created_at
created_by

2. Student: Represents an individual enrolling in the school/courses via the system.
-Relationships: Each student is able to enroll their details, to be linked to multiple enrollments.
-Fields:
first_name, last_name
email (unique)
phone_number
enrollment_date
created_by

3. AcademicYear: Represents the academic year of the enrollment
-Relationships: Linked to semesters and enrollments via a foreign key relation.
-Fields:
academic_year_name
start_date, end_date
created_at, updated_at
created_by

4. Course: Represents a field of study the student is being enrolled to.
-Relationships: A course is associated/linked with one school, and multiple students can enroll in courses.
-Fields:
title
code (unique)
description
credits
created_by
school

5. Semester: Represents a period within an academic year the student is being enrolled
-Relationships: Linked to the academic year the student enrolls.
-Fields:
name
start_date, end_date
academic_year
created_by

6.Enrollment: Represents the entry of user details into the system. Where if you are enrolled the data will be stored in the database
Relationships: Links a student to a school, course, and academic year.
Fields:
student, school, course, academic_year
enrollment_date
created_by

### viewsets

the viewset makes use of imports from the rest_framework, which allows the import of different functionaslities to be used in the system.

-SchoolListCreateView
This view handles listing all schools in the system and creating new school records.
It uses ListCreateAPIView, which combines listing and creation functionality.
it only allows authenticated users to access this endpoint, and only admin users create new records 

-SchoolRetrieveUpdateView
This view is for retrieving details of a specific school and/or updating an existing school.
It uses RetrieveUpdateAPIView, which allows fetching and updating individual records.
Only authenticated users can access this view, and updates are restricted to admins.

-StudentListCreateView
Provides functionality to list all students and create new student records.
When a new student is added, the created_by field links the record to the user who created it.

-StudentRetrieveUpdateView
Enables retrieval and update of a specific student’s information.

-AcademicYearListCreateView
This view manages the listing and creation of academic year records.
Only authenticated users can access the endpoint, but only admin or staff users are allowed to create new records.
During creation, the created_by field ensures that the record tracks the user responsible.

-AcademicYearRetrieveUpdateView
Handles retrieving details of a specific academic year and updating its data.
Only admins can perform updates, and all changes are linked to the user making the modification.

-CourseListCreateView
Manages listing all courses and creating new course records.
Authenticated users can access the data, but creation is restricted to admins or staff.
The perform_create method links the course to the user who created it.

-CourseRetrieveUpdateView
Allows retrieving the details of a specific course and updating its information.

-SemesterListCreateView
Provides functionality for listing all semesters and creating new semester records.
Authenticated access is required, and only admins can create new records.
Creation of new records track the user responsible using the created_by field.

-SemesterRetrieveUpdateView
Handles retrieving and updating specific semester details.
Updates are restricted to admins.

-EnrollmentListCreateView
Manages listing all enrollments and creating new enrollment records.
The perform_create method ensures the created_by field is set to the user making the request.

-EnrollmentRetrieveUpdateView
Allows fetching and updating the details of a specific enrollment.
Updates are limited to authenticated users, and changes are linked to the user performing the update.

-Signup View
This view enables new users to register an account in the system.
It accepts a POST request with a username and password in the request body.
If the username already exists, it returns an error message.
If the credentials are valid and unique, a new user is created, and a success message is returned.

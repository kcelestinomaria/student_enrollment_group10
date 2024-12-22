# Student Enrollment System API Documentation

Welcome to the **Student Enrollment System API** documentation! This guide provides comprehensive information about the API, its endpoints, and instructions to set up and test the project locally.

This API System is meant as group assignment for the course BBIT, unit API, at Strathmore University.
Here are the names of the students in the group assignment, who contributed:
1. Celestine Kariuki - Student No. 116533
2. Eghosa Edokpolo - Student No. 170492
3. Mohammed Mumin - Student No. 165700
4. Wayne Opanja - Student No. 166937
5. Amina Abigail - Student No. 100485
6. Mumo Mwangangi - Student No. 165437

---

## Table of Contents

1. [Overview](#overview)
2. [Installation](#installation)
3. [Environment Setup](#environment-setup)
4. [API Endpoints](#api-endpoints)
    - [Schools](#schools)
    - [Students](#students)
    - [Courses](#courses)
    - [Academic Years](#academic-years)
    - [Semesters](#semesters)
    - [Enrollments](#enrollments)
5. [Testing with Postman](#testing-with-postman)
6. [Contributing](#contributing)

---

## Overview

The **Student Enrollment System API** is built using Django and Django REST Framework (DRF). It enables managing schools, students, courses, academic years, semesters, and enrollments. The API features user authentication and role-based access for secure interaction.

---

## Installation

Follow these steps to clone and run the project locally:

### Prerequisites
Ensure the following are installed on your system:
- Python 3.8+
- pip (Python package manager)
- Git

### Clone the Repository

```bash
$ git clone https://github.com/your-repository/enrollment-system.git
$ cd enrollment-system
```

---

## Environment Setup

### 1. Create a Virtual Environment

```bash
$ python -m venv venv
$ source venv/bin/activate  # On Windows, use venv\Scripts\activate
```

### 2. Install Dependencies

```bash
$ pip install -r requirements.txt
```

### 3. Apply Migrations

```bash
$ python manage.py migrate
```

### 4. Create a Superuser

```bash
$ python manage.py createsuperuser
```

### 5. Run the Server

```bash
$ python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`.

---

## API Endpoints

### Authentication(Currently Disabled)

- You can go to Admin on this URL `POST /admin/`
 

### Schools
- **List/Create Schools**
  - `GET /api/schools/`
  - `POST /api/schools/`

- **Retrieve/Update a School**
  - `GET /api/schools/{id}/`
  - `PUT /api/schools/{id}/`

### Students
- **List/Create Students**
  - `GET /api/students/`
  - `POST /api/students/`

- **Retrieve/Update a Student**
  - `GET /api/students/{id}/`
  - `PUT /api/students/{id}/`

### Courses
- **List/Create Courses**
  - `GET /api/courses/`
  - `POST /api/courses/`

- **Retrieve/Update a Course**
  - `GET /api/courses/{id}/`
  - `PUT /api/courses/{id}/`

### Academic Years
- **List/Create Academic Years**
  - `GET /api/academicyears/`
  - `POST /api/academicyears/`

- **Retrieve/Update an Academic Year**
  - `GET /api/academicyears/{id}/`
  - `PUT /api/academicyears/{id}/`

### Semesters
- **List/Create Semesters**
  - `GET /api/semesters/`
  - `POST /api/semesters/`

- **Retrieve/Update a Semester**
  - `GET /api/semesters/{id}/`
  - `PUT /api/semesters/{id}/`

### Enrollments
- **List/Create Enrollments**
  - `GET /api/enrollments/`
  - `POST /api/enrollments/`

- **Retrieve/Update an Enrollment**
  - `GET /api/enrollments/{id}/`
  - `PUT /api/enrollments/{id}/`

---

## Testing with Postman(Included With Screenshots)
*(We used Postman Visual Studio Code Extension, as the desktop agent is buggy and heavy!)

![Postman As VS Code Extension](images/Screenshot%202024-12-20%20172322.png)
Figure 1: Postman As a VS Code Extension


![Postman In Action #2](images/Screenshot%202024-12-20%20172859.png)
Figure 2: Postman In Action Part 1

### Step 3: Test Endpoints

![Postman In Action #3](images/Screenshot%202024-12-20%20172939.png)
Figure 3: Postman In Action Part 2


![GET Student By ID](images/Screenshot%202024-12-20%20174326.png)
Figure 4: Get A Student By his/her ID


![GET All Students](images/Screenshot%202024-12-20%20174348.png)
Figure 5: Get All Students

#### Example: Create a School
1. Select the `POST /api/schools/` endpoint.
2. In the body, input:
   ```json
   {
     "school_name": "Strathmore University"
   }
   ```
3. Send the request.
4. Successful Response:
   ```json
   {
     "id": 1,
     "school_name": "Strathmore University",
     "created_at": "2024-12-19T12:00:00Z",
     "created_by": 1
   }
   ```
![UPDATE A Student's Details](images/Screenshot%202024-12-20%20184510.png)
Figure 6: Update A Student's Details using a PUT Request


![DELETE A Student's Details](images/Screenshot%202024-12-20%20183806.png)
Figure 7: Delete A Student By his/her ID


![GET All Student's Details After DELETE operation](images/Screenshot%202024-12-20%20184543.png)
Figure 8: Get All Student's Details After running the DELETE HTTP Action Method


## Admin Functionality
Also, here is the Admin, as we enter a Student's Data, with in-built validation:

![Enter Student Data & Get Validated](images/Admin-Data-Validation.png)
Figure 9: Enter Student Data, System Validates


Here is another image showing us having added data for all entities successfully:

![Enter Student, Dept, Course, Program & All Data](images/Admin-Succesful-Data-Add.png)
Figure 10: Enter All Enrollment System Data


## Successful Unit Testing
We also successfully ran Python Unit Tests:

![Successful Unit Tests](images/Test-Run-Succesful.png)
Figure 11: Successful Unit Testing Data

## Contributing

We welcome contributions to enhance the functionality of the API. Please follow these steps:
1. Fork the repository.
2. Create a feature branch.
3. Commit your changes and open a pull request.

---

Thank you for using the **Student Enrollment System API**! If you encounter any issues, please open an issue in the repository.


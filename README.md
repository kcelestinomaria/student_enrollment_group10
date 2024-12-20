# Student Enrollment System API Documentation

Welcome to the **Student Enrollment System API** documentation! This guide provides comprehensive information about the API, its endpoints, and instructions to set up and test the project locally.

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
$ git clone https://github.com/your-repository/student-enrollment-system.git
$ cd student-enrollment-system
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

### Authentication
- **Login**
  - `POST /api/token/`
  - Request:
    ```json
    {
      "username": "admin",
      "password": "password"
    }
    ```
  - Response:
    ```json
    {
      "access": "<access_token>",
      "refresh": "<refresh_token>"
    }
    ```

- **Signup**
  - `POST /api/signup/`
  - Request:
    ```json
    {
      "username": "newuser",
      "password": "newpassword"
    }
    ```
  - Response:
    ```json
    {
      "message": "User created successfully"
    }
    ```

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

### Step 1: Import the API Collection
1. Download the Postman collection file from the repository.
2. Open Postman and import the collection.
![Postman As VS Code Extension](images\Screenshot 2024-12-20 172322.png)


### Step 2: Authentication
1. Use the `POST /api/token/` endpoint to obtain an access token.
2. Add the token to the headers for authenticated requests:
   ```
   Authorization: Bearer <access_token>
   ```
![Postman In Action #2](images\Screenshot 2024-12-20 172859.png)

### Step 3: Test Endpoints

![Postman In Action #3](images\Screenshot 2024-12-20 172939.png)
Postman In Action

![GET Student By ID](images\Screenshot 2024-12-20 174326.png)
Get A Student By his/her ID


![GET All Students](images\Screenshot 2024-12-20 174348.png)
Get All Students

#### Example: Create a School
1. Select the `POST /api/schools/` endpoint.
2. In the body, input:
   ```json
   {
     "school_name": "Strathmore University"
   }
   ```
[Postman In Action #4]()
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
![UPDATE A Student's Details](images\Screenshot 2024-12-20 184510.png)
Update A Student's Details using a PUT Request


![DELETE A Student's Details](images\Screenshot 2024-12-20 183806.png)
Delete A Student By his/her ID

![GET All Student's Details After DELETE operation](images\Screenshot 2024-12-20 184543.png)
Get All Student's Details After running the DELETE HTTP Action Method

---

## Contributing

We welcome contributions to enhance the functionality of the API. Please follow these steps:
1. Fork the repository.
2. Create a feature branch.
3. Commit your changes and open a pull request.

---

Thank you for using the **Student Enrollment System API**! If you encounter any issues, please open an issue in the repository.


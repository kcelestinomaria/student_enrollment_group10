# Project Outline: Student Enrollment System
Inspired by the Strathmore Enrollment Process.
## 1. Models
The system will use the following models:

### School
**Fields:**
- `school_name`: Name of the school (unique).
- `created_at`: Timestamp when the school record was created.
- `created_by`: ForeignKey to User (tracks the user who created the record).

### Student
**Fields:**
- `first_name`, `last_name`: Name of the student.
- `email`: Unique email address for the student.
- `phone_number`: Contact number (max 13 characters).
- `enrollment_date`: Date of enrollment (auto-generated).
- `created_by`: ForeignKey to User.

### AcademicYear
**Fields:**
- `academic_year_name`: Name of the academic year (e.g., 2023/2024).
- `start_date`, `end_date`: Duration of the academic year.
- `created_at`, `updated_at`: Timestamps for record creation and modification.
- `created_by`: ForeignKey to User.

### Course
**Fields:**
- `title`: Title of the course.
- `code`: Unique code for the course.
- `description`: Brief overview of the course.
- `credits`: Credit value of the course.
- `school`: ForeignKey linking the course to a school.
- `created_by`: ForeignKey to User.

### Semester
**Fields:**
- `name`: Name of the semester (e.g., Fall 2024).
- `start_date`, `end_date`: Duration of the semester.
- `AcademicYear`: ForeignKey to the associated AcademicYear.
- `created_by`: ForeignKey to User.

### Enrollment
**Fields:**
- `student`: ForeignKey to the Student model.
- `school`: ForeignKey to the School model.
- `course`: ForeignKey to the Course model.
- `enrollment_date`: Date of enrollment.
- `AcademicYear`: ForeignKey to the AcademicYear.
- `created_by`: ForeignKey to User.

---

## 2. Serializers
Serializers will be created for all models to:

- Convert data between JSON and Python objects.
- Validate input data for constraints like unique values and date ranges.

---

## 3. Views/Viewsets

### Generic Viewsets
Each model will have corresponding viewsets to handle:

- **List/Create**: Retrieve a list of records or add a new one.
- **Retrieve/Update/Delete**: Perform operations on a single record by its ID.

### Custom Logic
For models like AcademicYear, validation logic (e.g., `start_date < end_date`) will be enforced in both the model's `clean` method and the serializer.

---

## 4. URLs
RESTful URLs will be structured as follows:

- `/schools/`: Manage school records.
- `/students/`: Manage student records.
- `/academic-years/`: Manage academic year records.
- `/courses/`: Manage course records.
- `/semesters/`: Manage semester records.
- `/enrollments/`: Manage enrollment records.

---

## 5. Testing

### Automated Tests

**Unit Tests:**
- Written using Django's `APITestCase`.

**Test Cases:**
- Validation for fields (e.g., email format, unique constraints).
- CRUD operations for each model.
- Relationship integrity (e.g., deleting a student does not cascade to unrelated models).

### Manual Tests
- Use tools like Postman to test APIs.
- Document results using screenshots and logs.

---

## 6. Deliverables

### GitHub Repository
- **Named:** `student_enrollment`.
- **Contains:**
  - Complete source code.
  - README with setup instructions.

### README File
Includes:
- Description of models and their relationships.
- Example requests/responses for each endpoint.
- Test results.

### Testing Evidence
- Logs or screenshots from Postman.
- Output of unit tests showing coverage and results.

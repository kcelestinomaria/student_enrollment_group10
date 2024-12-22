from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from .models import School, Student, Course, Department, Program, Enrollment, Instructor, ClassSession, Attendance


class SchoolModelTest(TestCase):
    def setUp(self):
        # Create a user to associate with the school
        self.user = User.objects.create_user(username='testuser', password='password')

    def test_school_creation(self):
        school = School.objects.create(
            school_name="School of Computing and Engineering Sciences",
            created_by=self.user
        )
        self.assertEqual(school.school_name, "School of Computing and Engineering Sciences")
        self.assertEqual(school.created_by, self.user)


class StudentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.department = Department.objects.create(department_code="CSE", department_name="Computer Science and Engineering", head_of_department="Dr. John Doe")
        self.program = Program.objects.create(program_code="CS101", program_name="Bachelor of Science in Computer Science", department=self.department)

    def test_student_creation(self):
        student = Student.objects.create(
            first_name="Celestine",
            last_name="Njoroge",
            email="celestine@example.com",
            phone_number="1234567890",
            program=self.program
        )
        self.assertEqual(student.first_name, "Celestine")
        self.assertEqual(student.last_name, "Njoroge")
        self.assertEqual(student.email, "celestine@example.com")
        self.assertEqual(student.phone_number, "1234567890")
        self.assertEqual(student.program, self.program)


class CourseModelTest(TestCase):
    def setUp(self):
        self.department = Department.objects.create(department_code="CSE", department_name="Computer Science and Engineering", head_of_department="Dr. John Doe")

    def test_course_creation(self):
        course = Course.objects.create(
            course_code="CS101",
            course_name="Introduction to Programming",
            description="This is a basic course on programming.",
            credits=3,
            department=self.department
        )
        self.assertEqual(course.course_code, "CS101")
        self.assertEqual(course.course_name, "Introduction to Programming")
        self.assertEqual(course.description, "This is a basic course on programming.")
        self.assertEqual(course.credits, 3)
        self.assertEqual(course.department, self.department)


class DepartmentModelTest(TestCase):
    def test_department_creation(self):
        department = Department.objects.create(
            department_code="CSE",
            department_name="Computer Science and Engineering",
            head_of_department="Dr. John Doe"
        )
        self.assertEqual(department.department_code, "CSE")
        self.assertEqual(department.department_name, "Computer Science and Engineering")
        self.assertEqual(department.head_of_department, "Dr. John Doe")


class ProgramModelTest(TestCase):
    def setUp(self):
        self.department = Department.objects.create(department_code="CSE", department_name="Computer Science and Engineering", head_of_department="Dr. John Doe")

    def test_program_creation(self):
        program = Program.objects.create(
            program_code="CS101",
            program_name="Bachelor of Science in Computer Science",
            department=self.department
        )
        self.assertEqual(program.program_code, "CS101")
        self.assertEqual(program.program_name, "Bachelor of Science in Computer Science")
        self.assertEqual(program.department, self.department)


class EnrollmentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.department = Department.objects.create(department_code="CSE", department_name="Computer Science and Engineering", head_of_department="Dr. John Doe")
        self.program = Program.objects.create(program_code="CS101", program_name="Bachelor of Science in Computer Science", department=self.department)
        self.student = Student.objects.create(
            first_name="Celestine",
            last_name="Njoroge",
            email="celestine@example.com",
            phone_number="1234567890",
            program=self.program
        )
        self.course = Course.objects.create(
            course_code="CS101",
            course_name="Introduction to Programming",
            description="This is a basic course on programming.",
            credits=3,
            department=self.department
        )

    def test_enrollment_creation(self):
        enrollment = Enrollment.objects.create(
            student=self.student,
            course=self.course,
            grade="A"
        )
        self.assertEqual(enrollment.student, self.student)
        self.assertEqual(enrollment.course, self.course)
        self.assertEqual(enrollment.grade, "A")


class InstructorModelTest(TestCase):
    def setUp(self):
        self.department = Department.objects.create(department_code="CSE", department_name="Computer Science and Engineering", head_of_department="Dr. John Doe")

    def test_instructor_creation(self):
        instructor = Instructor.objects.create(
            instructor_id="I123",
            first_name="Jane",
            last_name="Doe",
            email="jane.doe@example.com",
            department=self.department
        )
        self.assertEqual(instructor.instructor_id, "I123")
        self.assertEqual(instructor.first_name, "Jane")
        self.assertEqual(instructor.last_name, "Doe")
        self.assertEqual(instructor.email, "jane.doe@example.com")
        self.assertEqual(instructor.department, self.department)


class ClassSessionModelTest(TestCase):
    def setUp(self):
        self.department = Department.objects.create(department_code="CSE", department_name="Computer Science and Engineering", head_of_department="Dr. John Doe")
        self.course = Course.objects.create(
            course_code="CS101",
            course_name="Introduction to Programming",
            description="This is a basic course on programming.",
            credits=3,
            department=self.department
        )
        self.instructor = Instructor.objects.create(
            instructor_id="I123",
            first_name="Jane",
            last_name="Doe",
            email="jane.doe@example.com",
            department=self.department
        )

    def test_class_session_creation(self):
        class_session = ClassSession.objects.create(
            course=self.course,
            instructor=self.instructor,
            start_time=timezone.now(),
            end_time=timezone.now() + timezone.timedelta(hours=1),
            location="Room 101"
        )
        self.assertEqual(class_session.course, self.course)
        self.assertEqual(class_session.instructor, self.instructor)
        self.assertEqual(class_session.location, "Room 101")


class AttendanceModelTest(TestCase):
    def setUp(self):
        self.department = Department.objects.create(department_code="CSE", department_name="Computer Science and Engineering", head_of_department="Dr. John Doe")
        self.course = Course.objects.create(
            course_code="CS101",
            course_name="Introduction to Programming",
            description="This is a basic course on programming.",
            credits=3,
            department=self.department
        )
        self.student = Student.objects.create(
            first_name="Celestine",
            last_name="Njoroge",
            email="celestine@example.com",
            phone_number="1234567890",
            program=None
        )
        self.instructor = Instructor.objects.create(
            instructor_id="I123",
            first_name="Jane",
            last_name="Doe",
            email="jane.doe@example.com",
            department=self.department
        )
        self.class_session = ClassSession.objects.create(
            course=self.course,
            instructor=self.instructor,
            start_time=timezone.now(),
            end_time=timezone.now() + timezone.timedelta(hours=1),
            location="Room 101"
        )

    def test_attendance_creation(self):
        attendance = Attendance.objects.create(
            class_session=self.class_session,
            student=self.student,
            attendance_status="Present"
        )
        self.assertEqual(attendance.class_session, self.class_session)
        self.assertEqual(attendance.student, self.student)
        self.assertEqual(attendance.attendance_status, "Present")

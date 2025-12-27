"""
University System

Model a university system using composition. You are given the Student and
Professor classes. You must implement Department and University.

1. Student (Given):
   - __init__(self, name, student_id)
   - Has name and student_id attributes.

2. Professor (Given):
   - __init__(self, name, employee_id)
   - Has name and employee_id attributes.

3. Department (To Implement):
   - __init__(self, name): Initializes name, an empty list self.professors,
     and an empty list self.students.
   - add_professor(self, professor): Adds a Professor object to self.professors.
   - add_student(self, student): Adds a Student object to self.students.

4. University (To Implement):
   - __init__(self, name): Initializes name and an empty list self.departments.
   - add_department(self, department): Adds a Department object to self.departments.
   - get_students_in_department(self, dept_name): Returns a list of Student
     objects in the department with that name.
   - get_all_students(self): Returns a list of all Student objects in the
     entire university, across all departments.
"""

# I AM NOT DONE


class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def __repr__(self):
        return f"Student({self.name}, {self.student_id})"


class Professor:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def __repr__(self):
        return f"Professor({self.name}, {self.employee_id})"


class Department:
    pass


class University:
    pass


# ============================================================================
# Tests - Do not modify below this line
# ============================================================================
def test_department():
    dept = Department("Computer Science")
    assert dept.name == "Computer Science"
    assert dept.professors == []
    assert dept.students == []

    prof = Professor("Dr. Smith", "E001")
    dept.add_professor(prof)
    assert len(dept.professors) == 1

    student = Student("Alice", "S001")
    dept.add_student(student)
    assert len(dept.students) == 1


def test_university():
    uni = University("Imperial College")
    assert uni.name == "Imperial College"
    assert uni.departments == []

    cs_dept = Department("Computer Science")
    cs_dept.add_student(Student("Alice", "S001"))
    cs_dept.add_student(Student("Bob", "S002"))

    math_dept = Department("Mathematics")
    math_dept.add_student(Student("Charlie", "S003"))

    uni.add_department(cs_dept)
    uni.add_department(math_dept)

    cs_students = uni.get_students_in_department("Computer Science")
    assert len(cs_students) == 2

    all_students = uni.get_all_students()
    assert len(all_students) == 3


if __name__ == "__main__":
    test_department()
    test_university()
    print("All tests passed!")

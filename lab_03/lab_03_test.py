import pytest
from student import Student
from studentList import StudentList
from utils import Utils

@pytest.fixture
def fixStudents():
    studentList = StudentList()
    studentList.addNewElement(Student("Sofi", "0631234567", "sofi@gmail.com", "cs-95"))
    return studentList

def test_addNewElement(fixStudents):
    initialLen = len(fixStudents.students)
    fixStudents.addNewElement(Student("John", "1234567890", "john@gmail.com", "cs-101"))
    assert len(fixStudents.students) == initialLen + 1
    assert any(student.name == "John" for student in fixStudents.students)

def test_updateNewElement(fixStudents):
    fixStudents.updateElement("Sofi", "group", "cs-45")
    updatedStudent = next(student for student in fixStudents.students if student.name == "Sofi")
    assert updatedStudent.group == "cs-45"

def test_deleteElement(fixStudents):
    initialLen = len(fixStudents.students)
    fixStudents.deleteElement("Sofi")
    assert len(fixStudents.students) == initialLen - 1
    assert not any(student.name == "Sofi" for student in fixStudents.students)

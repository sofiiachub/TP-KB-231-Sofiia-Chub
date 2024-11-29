import pytest
from lab_02 import studentList, addNewElement, deleteElement, updateElement

def test_add_new_element():
    initial_len = len(studentList)
    addNewElement()
    assert len(studentList) == initial_len + 1
    assert any(student["name"] == "Sofi" for student in studentList)

def test_update_element():
    updateElement()
    updated_student = next(student for student in studentList if student["name"] == "Sofi")
    assert updated_student["group"] == "cs-45"

def test_delete_element():
    initial_len = len(studentList)
    deleteElement()
    assert len(studentList) == initial_len - 1
    assert not any(student["name"] == "Sofi" for student in studentList)
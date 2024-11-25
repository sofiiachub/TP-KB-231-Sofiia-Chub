class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, age: {self.age})"

students = [
    Student("Tim", 20),
    Student("David", 13),
    Student("Vlada", 11),
    Student("Olena", 54)
]

sorted_students = sorted(students, key=lambda student: student.name)
print("Student list")

for student in sorted_students:
    print(student)
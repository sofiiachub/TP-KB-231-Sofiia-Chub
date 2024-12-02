class StudentList:
    def __init__(self):
        self.students = []

    def printAllList(self):
        for student in self.students:
            print(student)

    def addNewElement(self, student):
        insertPosition = 0
        for item in self.students:
            if student.name > item.name:
                insertPosition += 1
            else:
                break
        self.students.insert(insertPosition, student)
        print("New element has been added")

    def deleteElement(self, name):
        student = next((s for s in self.students if s.name == name), None)
        if student:
            self.students.remove(student)  # Пряме видалення студента зі списку
            print(f"Deleted student: {student.name}")
        else:
            print("Student not found.")

    def updateElement(self, name, attribute, newValue):
        student = next((s for s in self.students if s.name == name), None)
        if student:
            match attribute:
                case "name":
                    student.name = newValue
                case "phone":
                    student.phone = newValue
                case "gmail":
                    student.gmail = newValue
                case "group":
                    student.group = newValue
                case _:
                    print(f"Unknown attribute: {attribute}")
        else:
            print("Student not found.")

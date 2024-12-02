import csv
from student import Student
from studentList import StudentList

class Utils:
    def loadDataCSV(self, filename):
        studentList = StudentList()
        try:
            with open(filename, 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=';')
                for row in reader:
                    student = Student(row["name"], row["phone"], row["gmail"], row["group"])
                    studentList.addNewElement(student)
            print(f"The data from {filename} was loaded successfully.")
            return studentList
        except Exception as e:
            print(f"Error loading data from {filename}: {e}")
            return studentList

    def saveDataCSV(self, filename, studentList):
        try:
            with open(filename, 'w', newline='') as csvfile:
                fieldnames = ['name', 'phone', 'gmail', 'group']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
                writer.writeheader()
                for student in studentList.students:
                    writer.writerow({
                        'name': student.name,
                        'phone': student.phone,
                        'gmail': student.gmail,
                        'group': student.group
                    })
            print(f"Data has been successfully saved to {filename}.")
        except Exception as e:
            print(f"Error saving data to {filename}: {e}")
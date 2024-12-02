import sys
from utils import Utils
from studentList import StudentList
from student import Student

def main():
    filename = "studentsData.csv"
    studentList = StudentList()
    forFileCVS = Utils()

    if len(sys.argv) > 1:
        studentList = forFileCVS.loadDataCSV(sys.argv[1])

    while True:
        choice = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")

        match choice:
            case "C" | "c":
                name = input("Please enter student name: ")
                phone = input("Please enter student phone: ")
                gmail = input("Please enter student gmail: ")
                group = input("Please enter student group: ")

                student = Student(name, phone, gmail, group)
                studentList.addNewElement(student)
                studentList.printAllList()

            case "U" | "u":
                name = input("Please enter name to be updated: ")
                attribute = input("What data do you want to change (name|phone|gmail|group): ")
                newValue = input(f"Enter new value for {attribute}: ")
                studentList.updateElement(name, attribute, newValue)
                studentList.printAllList()

            case "D" | "d":
                name = input("Please enter name to be deleted: ")
                studentList.deleteElement(name)
                studentList.printAllList()

            case "P" | "p":
                studentList.printAllList()

            case "X" | "x":
                print("Exiting()")
                forFileCVS.saveDataCSV(filename, studentList)
                break

            case _:
                print("Wrong choice.")

if __name__ == '__main__':
    main()

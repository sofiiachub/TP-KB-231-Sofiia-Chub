# add new modules
import csv 
import sys 

studentList = [
    # added parameters "gmail" and "group" in list
    {"name":"Bob", "phone":"0631234567", "gmail":"bobby@gmail.com", "group":"cs-44"},
    {"name":"Emma", "phone":"0631234567", "gmail":"emmy@gmail.com", "group":"cs-51"},
    {"name":"Jon",  "phone":"0631234567", "gmail":"johnny@gmail.com", "group":"cs-63"},
    {"name":"Zak",  "phone":"0631234567", "gmail":"zakky@gmail.com", "group":"cs-90"}
]

def loadDataCSV(filename):
    try:
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                print(row)
                newItem = {
                    "name": row["name"],
                    "phone": row["phone"],
                    "gmail": row["gmail"],
                    "group": row["group"]
                }
                studentList.append(newItem)
            studentList.sort(key=lambda x: x['name'])
        print(f"The data from the {filename} was loaded successfully.")
    except Exception as e:
        print(f"Error loading data to {filename}: {e}")

# saving date to a CSV file
def saveDataCSV(filename):
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['name', 'phone', 'gmail', 'group']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
            writer.writeheader()
            writer.writerows(studentList)
        print(f"Data has been successfully saved to {filename}.")
    except Exception as e:
        print(f"Error saving data to {filename}: {e}")

def printAllList():
    for elem in studentList:
        # added parameters "gmail" and "group" for print all list
        strForPrint = "Student name is " + elem["name"] + ",  Phone is " + elem["phone"] + ", Gmail is " + elem["gmail"] + ", Group is " + elem["group"]
        print(strForPrint)
    return

def addNewElement():
    # added parameters "gmail" and "group" for add new element
    name = input("Pease enter student name: ")
    phone = input("Please enter student phone: ")
    gmail = input("Please enter student gmail: ")
    group = input("Please enter student group: ")
    newItem = {"name": name, "phone": phone, "gmail": gmail, "group": group}

    insertPosition = 0
    for item in studentList:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    studentList.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElement():
    name = input("Please enter name to be delated: ")
    deletePosition = -1
    for item in studentList:
        if name == item["name"]:
            deletePosition = studentList.index(item)
            break

    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Dele position " + str(deletePosition))
        del studentList[deletePosition]
    return

def updateElement():
    # the date change function is implemented
    name = input("Please enter name to be updated: ")

    studentNames = [elem["name"] for elem in studentList]

    if name in studentNames:
        for elem in studentList:
            if elem["name"] == name:
                print("Current information about the student")
                strForPrint = "Name: " + elem["name"] + "\n  Phone: " + elem["phone"] + "\n  Gmail: " + elem["gmail"] + "\n  Group: " + elem["group"]
                print(strForPrint)

                choice = input("What data do you want to change (name|phone|gmail|group): ")

                match choice:
                     case "name":
                        newName = input("Enter a new name: ")

                        studentList.remove(elem)
                        newItem = {"name": newName, "phone": elem["phone"], "gmail": elem["gmail"], "group": elem["group"]}

                        insertPosition = 0
                        for item in studentList:
                            if newName > item["name"]:
                                insertPosition += 1
                            else:
                                break
                        studentList.insert(insertPosition, newItem)

                     case "phone":
                        newPhone = input("Enter a new phone: ")
                        elem["phone"] = newPhone
                     case "gmail":
                        newGmail = input("Enter a new gmail: ")
                        elem["gmail"] = newGmail
                     case "group":
                        newGroup = input("Enter a new group: ")
                        elem["group"] = newGroup
                     case _:
                        print("You didn't choose from the proposed options")
                        break
            else:
                print("Name not found")

    printAllList()
    return

def main():

    filename = "C:\\Users\\Nick\\Desktop\\GitHubTesting\\TP-KB-231-Sofiia-Chub\\lab_02\\studentsData.csv"
    if len(sys.argv) > 1:
        loadDataCSV(sys.argv[1])

    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Existing element will be updated")
                updateElement()
            case "D" | "d":
                print("Element will be deleted")
                deleteElement()
            case "P" | "p":
                print("List will be printed")
                printAllList()
            case "X" | "x":
                print("Exit()")
                saveDataCSV(filename)
                break
            case _:
                print("Wrong chouse")

if __name__ == '__main__':
    main()
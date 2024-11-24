list = [
    # added parameters "gmail" and "group" in list
    {"name":"Bob", "phone":"0631234567", "gmail":"bobby@gmail.com", "group":"cs-44"},   
    {"name":"Emma", "phone":"0631234567", "gmail":"emmy@gmail.com", "group":"cs-51"},
    {"name":"Jon",  "phone":"0631234567", "gmail":"johnny@gmail.com", "group":"cs-63"},
    {"name":"Zak",  "phone":"0631234567", "gmail":"zakky@gmail.com", "group":"cs-90"}
]

def printAllList():
    for elem in list:
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
    for item in list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    list.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElement():
    name = input("Please enter name to be delated: ")
    deletePosition = -1
    for item in list:
        if name == item["name"]:
            deletePosition = list.index(item)
            break
    
    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Dele position " + str(deletePosition))
        del list[deletePosition]
    return

def updateElement():
    # the date change function is implemented
    name = input("Please enter name to be updated: ")

    studentNames = [elem["name"] for elem in list]
    
    if name in studentNames:
        for elem in list:
            if elem["name"] == name:
                print("Current information about the student")
                strForPrint = "Name: " + elem["name"] + "\n  Phone: " + elem["phone"] + "\n  Gmail: " + elem["gmail"] + "\n  Group: " + elem["group"]
                print(strForPrint)

                choice = input("What data do you want to change (name|phone|gmail|group): ")
                
                match choice:
                     case "name":
                        newName = input("Enter a new name: ")

                        list.remove(elem)
                        newItem = {"name": newName, "phone": elem["phone"], "gmail": elem["gmail"], "group": elem["group"]}

                        insertPosition = 0
                        for item in list:
                            if newName > item["name"]:
                                insertPosition += 1
                            else:
                                break
                        list.insert(insertPosition, newItem)
                
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
                break
            case _:
                print("Wrong chouse")

main()
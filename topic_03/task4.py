def findPosition(numberList, number): 
    insertPosition = 0 
    for item in numberList: 
        if number > item: 
            insertPosition += 1 
        else: 
            break 
    return insertPosition 

numberList = [1, 3, 4, 2, 9, 10] 
numberList.sort() 
print("Наш сортований лист:", numberList) 

number = int(input("Введіть число: ")) 

position = findPosition(numberList, number) 
print("Позиція вставки:", position) 

numberList.insert(position, number) 
print("Оновлений лист:", numberList) 

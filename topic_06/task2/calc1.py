from functions1 import addd, subtract, multiply, divide
from operations1 import myinput, operation, recordHistory

start = input("This is a calculator. Will we start? (Yes/No): ")

while start.lower() == "yes":
    num1, num2, operation1 = myinput()

    if num1 is not None and num2 is not None and operation1 in ['+', '-', '*', '/']:
        result = operation(num1, num2, operation1, addd, subtract, multiply, divide)
        print("Result:", result)
        recordHistory(num1, num2, operation1, result, True)
    else:
        print("Invalid input, please try again.")
        recordHistory(num1, num2, operation1, "Invalid input", False)

    start = input("Will we continue the work? (Yes/No): ")
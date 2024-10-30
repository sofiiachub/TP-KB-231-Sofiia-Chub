def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error. Division by zero"

def calculator(num1, num2, operation):
    match operation:
        case "+":
            return add(num1, num2)
        case "-":
            return subtract(num1, num2)
        case "*":
            return multiply(num1, num2)
        case "/":
            return divide(num1, num2)
        case _:
            return "Error"

start = input("This is a calculator. Will we start? (Yes/No): ")

while start == "Yes":
    try:
        num1 = float(input("What's a: "))
        num2 = float(input("What's b: "))

        operation = input("Select an option (+, -, *, /): ")
        if operation not in ["+", "-", "*", "/"]:
            print("An invalid operation was entered")
        else:
            result = calculator(num1, num2, operation)
            print("Result:", result)
    
    except ValueError:
        print("Is not a number")

    start = input("Will we continue the work? (Yes/No): ")
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
        return "Error. Division by zero."

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
            return "Error."

num1 = int(input("What`s a: "))
num2 = int(input("What`s b: "))
operation = input("Select an option (+, -, *, /): ")

result = calculator(num1, num2, operation)  
print("Result:", result)


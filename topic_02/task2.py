
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
        return "Error: Division by zero."

def calculator(num1, num2, operation):

    if operation == "+":
        result = add(num1, num2)
    elif operation == "-":
        result = subtract(num1, num2)
    elif operation == "*":
        result = multiply(num1, num2)
    elif operation == "/":
        result = divide(num1, num2)
    else:
        result = "Error."

    return result

num1 = int(input("What's a: "))
num2 = int(input("What's b: "))
operation = input("Select an option (+, -, *, /): ")

result = calculator(num1, num2, operation)
print("Result:", result)

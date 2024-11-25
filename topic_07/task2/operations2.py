def myinput():
    try:
        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))
        operationn = input("Select an operation (+, -, *, /): ")
        return num1, num2, operationn
    except ValueError:
        print("Error: Invalid input. Please enter valid numbers.")
        return None, None, None

def myoperation(num1, num2, operationn, pluss, subtract, multiply, divide):
    match operationn:
        case "+":
            return pluss(num1, num2)
        case "-":
            return subtract(num1, num2)
        case "*":
            return multiply(num1, num2)
        case "/":
            try:
                return divide(num1, num2)
            except ZeroDivisionError:
                return "Error: Division by zero"
        case _:
            return "Incorrect operation. Please use +, -, *, or /."

def myinput():
    print("Enter two numbers: ")
    try:
        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))
        operation = input("Select an operation (+, -, *, /): ")
        return num1, num2, operation
    except ValueError:
        print("Error: Invalid input. Please enter numbers.")
        return None, None, None

def operation(num1, num2, operation, add, subtract, multiply, divide):
    if num1 is None or num2 is None:
        return "Invalid input, cannot perform operation."
    
    match operation:
        case "+":
            return add(num1, num2)
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

def recordHistory(num1, num2, operation1, result, trueDate):
    if trueDate:
        with open("fileActions", "a") as file:
            file.write(f"\tYour Action:\n")
            file.write(f"{num1} {operation1} {num2} = {result}\n")
    else:
        with open("fileMistakes", "a") as file:
            file.write(f"Invalid input or operation. num1: {num1}, num2: {num2}, operation: {operation1}\n")
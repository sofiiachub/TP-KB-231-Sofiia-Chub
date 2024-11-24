def myinput():
    print("Enter two numbers: ")
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    operation = input("Select an operation (+, -, *, /): ")

    return num1, num2, operation

def operation(num1, num2, operation, add, subtract, multiply, divide):
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
            return "Incorrect operations"
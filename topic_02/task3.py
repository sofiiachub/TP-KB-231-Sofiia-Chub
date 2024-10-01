
def calculator(num1, num2, operation):

    match operation:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            if num2 != 0:
                return num1 / num2
            else:
                return "Error. Division by zero."
        case _:
            return "Error."


num1 = int(input("What`s a: "))
num2 = int(input("What`s b: "))

operation = input("Select an option (+, -, *, /): ")
  
result = calculator(num1, num2, operation)  
print("Result:", result) 


from functions import add, subtract, multiply, divide
from operations import myinput, operation

def main():
    num1, num2, operation1 = myinput()
    result = operation(num1, num2, operation1, add, subtract, multiply, divide)
    print("Result:", result)

if __name__ == "__main__":
    main()
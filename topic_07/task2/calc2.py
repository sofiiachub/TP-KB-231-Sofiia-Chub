from functions2 import pluss, subtract, multiply, divide
from operations2 import myinput, myoperation

class Calculator:
    def __init__(self):
        self.file = "fileActions2"

    def addHistory(self, num1, num2, operationn, result):
        with open(self.file, "a") as file:
            file.write(f"{num1} {operationn} {num2} = {result}\n")

    def start(self):
        while True:
            num1, num2, operationn = myinput()

            if num1 is not None and num2 is not None:
                result = myoperation(num1, num2, operationn, pluss, subtract, multiply, divide)
                print(f"Result: {result}")

                self.addHistory(num1, num2, operationn, result)
            else:
                print("Invalid input, please try again.")

            continueWork = input("Do you want to continue? (Yes/No): ").lower()
            if continueWork != "yes":
                print("History is recorded")
                break

if __name__ == "__main__":
    calc = Calculator()
    calc.start()
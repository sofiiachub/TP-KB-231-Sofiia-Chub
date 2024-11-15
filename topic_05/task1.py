import random

def checkTheAnswer(choice, result):
    if choice == result:
        return "Draw"
    elif (choice == "stone" and result == "scissor") or (choice == "scissor" and result == "paper") or (choice == "paper" and result == "stone"):
        return "Winner: user"
    else:
        return "Winner: computer"

choice = input("Choose stone or scissor or paper: ")
result = random.choice(["stone", "scissor", "paper"])
print("Computer chose:", result)
print(checkTheAnswer(choice, result))

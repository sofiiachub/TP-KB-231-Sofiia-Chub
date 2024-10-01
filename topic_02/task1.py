
import math

def askParameters():
    a = int(input("What's a: "))
    b = int(input("What's b: "))
    c = int(input("What's c: "))
    return a, b, c


def calcDiscriminant(a, b, c):
    D = (b ** 2) - 4 * a * c
    return D


def calcRoots(a, b, c, D):
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        return x1, x2
    elif D == 0:
        x = -b / (2 * a)
        return x
    else:
        root = "There are no"
        return root


param1, param2, param3 = askParameters()
discriminant = calcDiscriminant(param1, param2, param3)
roots = calcRoots(param1, param2, param3, discriminant)

print("Roots :", roots)


def askParameters(): 
    a = int(input("What's a: ")) 
    b = int(input("What's b: ")) 
    c = int(input("What's c: ")) 
    return a, b, c 
 
def calcDiscriminant(a, b, c): 
    result = (b ** 2) - 4 * a *c 
    return result 
 
param1, param2, param3 = askParameters() 
result = calcDiscriminant(param1, param2, param3) 
 
print("Discriminant =", result)
pincilCase = {'pen': 3, 'pencil': 5, 'eraser': 2, 'ruler': 1}  
print(pincilCase)  

pincilCase.update({'sharpener': 4, 'pen': 6})  
print(pincilCase) 

del pincilCase['eraser'] 
print(pincilCase)  

print(pincilCase.keys())  
print(pincilCase)  

print(pincilCase.values())   
print(pincilCase)  

print(pincilCase.items())   
print(pincilCase)  

pincilCase.clear()  
print(pincilCase) 

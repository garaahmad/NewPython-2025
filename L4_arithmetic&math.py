frindes = 0
print(frindes)
frindes = frindes +1 #=1
frindes+=1 #=2
print(frindes)

frindes = frindes -1 
frindes-=1 
print(frindes)

frindes = frindes *2 
frindes*=2 
print(frindes)

frindes = frindes /2 
frindes/=2 
print(frindes)

frindes = frindes **2 #power
frindes**=2 
print(frindes)

frindes = frindes %2 
frindes%=2 
print(frindes)

#-------Math_______
x = 3.14
y =-4
z = 5

# result = round(x)
# result = abs(y)
# result = pow(4,3)
result = max(x,y,z)
result = min(x,y,z)

print(result)

import math
print(math.pi)
print(math.e)
# result=math.sqrt(5)
result =math.ceil(3.3)
result =math.floor(3.9)
print(result)


#Quiz1
radius = float(input("Enter Radius: "))
circumference =2*math.pi * radius
print(f"{round(circumference)}cm")

#Quiz2
radius = float(input("Enter Radius: "))
aria =math.pi * pow(radius,2)
print(f"The Area of circle is {round(aria)}cm")

#Quiz3
a = float(input('Enter side A: '))
b = float(input('Enter side B: '))
c = math.sqrt(pow(a,2) + pow(b,2))
print(f'Side c = {c}')



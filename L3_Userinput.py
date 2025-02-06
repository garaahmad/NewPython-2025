name = input('What is you name? ')
age = int(input('How old are you? '))
print(f'Hello {name}')
age = age +1
print("Happy Birthday")
print(f'you are {age} years old')

print("_"*50)

print('This is Calc to Know area Rectangle')
length = float(input('Enter Length in cm: '))
width = float(input('Enter Width in cm: '))
print(f'The area is :{length*width} cm')

print("_"*50)


item = input('What item would you like to buy?: ')
price = float(input("What is the Price?: "))
quantity = int(input('How many would you like?: '))
total = price * quantity
print(f'you have bought {quantity} X {item}/s')
print(f'Your total is:${total}')
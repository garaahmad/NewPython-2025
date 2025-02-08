name = input('Enter your name: ')
while name == '':
    print('you did not enter your name')
    name = input('Enter your name: ')
else:
    print(f'Hello {name}')
    
age = int(input('Enter your age: '))
while age < 0:
    print('Age cont\'s be negative')
    age = int(input('Enter your age: '))
print(f'your are {age} years old')

food = input('Enter a food you like (q to quit): ')
while not food == 'q':
    print(f'you Like : {food}')
    food = input('Enter a food you like (q to quit): ')
print('BYE')

num = int(input('Enter a # between 1 - 10: '))
while num < 1 or num > 10:
    print(f'{num} is not Valid')
    num = int(input('Enter a # between 1 - 10: '))
print(f'your number is {num}')
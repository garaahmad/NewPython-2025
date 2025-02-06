age = int(input('Enter you age: '))
if age >=100:
    print('you are too old to sign up')
elif age >=18:
    print('you are now signed up')
elif age <0:
    print('you haven\'t been born yet')

else:
    print('you must be 18+ to sign up')
    
    
print('_'*50)

response = input('Would you like food? (Y/N)')
if response =="Y":
    print('Have some food!!')
else: 
    print('Have not food!!')
    
print('_'*50)

name = input('Enter your name: ')
if name =='':
    print('You did not Enter your name!')
else:
    print(f"Hello{name}")
    
print('_'*50)
    
for_sale = True
if for_sale:
    print('This item is for sale')
else:
    print('This item is not for sale')
    
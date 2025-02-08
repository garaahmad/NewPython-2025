price1 = 3.14159
price2 = -987.65
price3 = 12.34
print(f'Price 1 is ${price1:.2f}')
print(f'Price 1 is ${price2:.2f}')
print(f'Price 1 is ${price3:.2f}')
print('_'*50)

print(f'Price 1 is ${price1:10}')#10space 
print(f'Price 1 is ${price2:10}')#10space
print(f'Price 1 is ${price3:10}')#10space
print('_'*50)

print(f'Price 1 is ${price1:010}')#10 zero Add 
print(f'Price 1 is ${price2:010}')#10 zero Add
print(f'Price 1 is ${price3:010}')#10 zero Add
print('_'*50)

print(f'Price 1 is ${price1:<10}') #____This is defult
print(f'Price 1 is ${price2:<10}')
print(f'Price 1 is ${price3:<10}')
print('_'*50)

print(f'Price 1 is ${price1:>10}') 
print(f'Price 1 is ${price2:>10}')
print(f'Price 1 is ${price3:>10}')
print('_'*50)

print(f'Price 1 is ${price1:^10}') #____To centrline
print(f'Price 1 is ${price2:^10}')
print(f'Price 1 is ${price3:^10}')
print('_'*50)

print(f'Price 1 is ${price1:+}') #return the + if num is positive
print(f'Price 1 is ${price2:+}') #return the - if num is negative
print(f'Price 1 is ${price3:+}')
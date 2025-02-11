numbers = [1,2,3,4,5]

for number in numbers:
    print(number ,end=" ")
print()
print("_______________")
for number in reversed(numbers):
    print(number ,end=" ")


# __________________________________
numbers = (1,2,3,4,5)

for number in numbers:
    print(number ,end=" ")
print()
print("_______________")
for number in reversed(numbers):
    print(number ,end=" ")
    
    
# _________________________________________

numbers = {1,2,3,4,5}

for number in numbers:
    print(number ,end=" ")
print()
print("_______________")
# for number in reversed(numbers):#EROOR 'set' object is not reversible
#     print(number ,end=" ")

# _________________________________________
name = 'Ahmad Omer'
for character in name:
    print(character ,end="  ")
    
    
print()
# _________________________________________
my_dict ={'A' : 1 , 'B' : 2 ,'c' : 3}
for value in my_dict.values():
    print(value)

for key,value in my_dict.items():
    print(f'{key} = {value}')
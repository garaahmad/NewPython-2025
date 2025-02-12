doubles = []
for x in range(1,11):
    doubles.append(x *2)

print(doubles)

#new way 
# [expression for value in iterable if cobdition]
doubles = [x*2 for x in range(1,11)]
triples = [x *3 for x in range(1,11)]
print(doubles)
print(triples)

fruits = ['apple','orangen','banana','coconut']
fruits = [fruit.upper() for fruit in fruits]
print(fruits)


#OR---------------

fruits = [fruit.upper() for fruit in ['apple','orangen','banana','coconut']]
print(fruits)



numbers = [1,2,3,-9,-8,-1,8,7,5]
positive_number = [num for num in numbers if num>0]
negative_number =[num for num in numbers if num<0]
even_number = [num for num in numbers if num%2==0]
odd_number = [num for num in numbers if num%2==1]
print(positive_number)
print(negative_number)
print(even_number)
print(odd_number)

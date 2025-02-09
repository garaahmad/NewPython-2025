#------------------------#List#------------------------#
fruits = ['apple' , 'orange','banana','coconut']
print(fruits)
print(fruits[2])
print(fruits[:3])
print(fruits[::2])
print(fruits[::-1])

for fruit in fruits:
    print(fruit)


#Return the number of items in a container.
print(len(fruits))

#chick if element in List
print('apple' in fruits)

#change element form List by index
fruits[0]='pineapple'
print(fruits)

#add element in end list
fruits.append('apple')
print(fruits)

#remove element from List if found
fruits.remove('apple')
print(fruits)

#add element in spacafec index
fruits.insert(0,'pineapple')
print(fruits)

#Sort the list in ascending order
fruits.sort()
print(fruits)

#Sort the list in desending order 
fruits.reverse()
print(fruits)

#return index >> if not fount return ERROR
print(fruits.index('banana'))

#Return number of occurrences of value
print(fruits.count('banana'))

#to remove all element
fruits.clear()


# ------------------------#SET#------------------------#

fruits = {'apple' , 'orange','banana','coconut'}
print(fruits) #is unordered

# #Return the number of items in a container.
print(len(fruits))


# #chick if element in Set 
print('apple' in fruits)

##Remove an element from a set; 
fruits.add('pineapple')
print(fruits)

#Remove an element from a set; it must be a member.
fruits.remove('pineapple')
print(fruits)

#remove Random element from a set
fruits.pop()
print(fruits)
#Remove all elements from a set; 
fruits.clear()
print(fruits)


# if the list have the two same element it remove one
fruits.add('pineapple')
print(fruits)



#------------------------#Tuple#------------------------#
fruits = ('apple' , 'orange','banana','coconut')

# # #Return the number of items in a container.
print(len(fruits))


# # #chick if element in Set 
print('apple' in fruits)

# #return index >> if not fount return ERROR
print(fruits.index('banana'))
# print(fruits.index('Ahmad')) Error

# #Return number of occurrences of value
print(fruits.count('banana'))
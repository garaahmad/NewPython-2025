fruits = ['apple' , 'orange','banana','coconut']
vegetables = ['celery' , 'carrots' , 'potatoes']
meats = ['chicken' , 'fish' , 'turkey']

groceries =[fruits,vegetables,meats]
print(groceries)
print(groceries[0])
print(groceries[0][1])

for row in groceries:
    for column in row:
        print(column,end=" , ")
    print()

num_pad = ((1,2,3),(4,5,6),(7,8,9),('*',0,'#'))
for row in num_pad:
    for column in row:
        print(column,end="  ")
    print()
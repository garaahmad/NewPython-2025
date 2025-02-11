def add1(a,b):
    return a+b

print(add1(1,2))

# print(add1(1,2,3))ERROR
#---------------------
def add2(*nums):#you can chang (*nums)but the important is (*)
    total = 0
    for arg in nums:
        total+=arg
    return total
print(add2(1,2,3))
print(add2(1,2,3,5,3,7))
print(add2(1,2,3,7,8,2,3,5,9,5))
print(add2(1,2,3,8,5,2,6,4))
print(add2(1,2,3,3,2,5,6,9,7,2,65,6,6,5,65,65,6))

def display_name(*names):
    for name in names:
        print(f'Hello {name}',end=" ")

display_name("Ahmad","Ali" ,"Omer")


def print_name(**kwargs):
    for key,value in kwargs.items():
        print(f'{key} : {value}')

print_name(first = "Ahmad" ,title ="MS" , last ='Omer')


def shipping_label(*args , **kwargs):
    for arg in args:
        print(arg,end=' ')
    
    if 'apt' in kwargs:
            print(f'{country} : {street} ,{apt}')
    else:
            print(f'{country} : {street}')

        
firstname = input('Enter your first name: ')
lastname = input('Enter your last name: ')

country = input('Enter your country: ')
street = input('Enter the street: ')
city = input('Enter the city: ')
state = input('Enter the state: ')
zipa = input('Enter the ZIP: ')
apt = input('Enter the APT: ')
shipping_label(firstname,lastname,country = country,street =street,city=city,state=state,zipa = zipa,apt = apt)



def hello(greeting , title , first , last):
    print(f'{greeting} {title} {first} {last}')
    
hello("Hello" , 'MR' , "Ahmad" ,"Algarably")
hello("Hello" , title='MR' , first="Ahmad", last="Algarably") #IT is Keyword argument
hello("HI" , last="Algarably",title='MR' , first="Ahmad" )


for x in range(1,11):
    print(x,end=" ")
print()
print('1','2','3','4','5','6','7','8','9' ,sep='--')

def getphone(country , area , frist , last):
    return f'{country}-{area}-{frist}-{last}'
phone_num = getphone(country= 1, area= 123, frist= 456, last=7890)
print(phone_num)
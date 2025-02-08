principle = 0
rate = 0
time = 0
while principle <= 0 :
     principle = float(input('Enter The principle amount: '))
     if principle <= 0:
         print('principle cant be less than or equla to zero \nEnter again')  
                
while rate <= 0 :
     rate = float(input('Enter The rate amount: '))
     if rate <= 0:
         print('rate cant be less than or equla to zero \nEnter again')  

while time <= 0 :
     time = int(input('Enter The time amount(Time in years): '))
     if time <= 0:
         print('time cant be less than or equla to zero \nEnter again')  


total = principle * pow((1+rate/100),time)
print(f'Balance after {time} year/s: ${total:.2f}')
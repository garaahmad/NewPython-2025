operator = input("Enter an Operator (+,-,*,/,%)")
num_1= float(input('Enter number 1: '))
num_2= float(input('Enter number 2: '))

if operator == '+':
    print(f"the Result is : {num_1+num_2}")
elif operator == '-':
    print(f"the Result is : {num_1-num_2}")
elif operator == '*':
    print(f"the Result is : {num_1*num_2}")
elif operator == '/':
    print(f"the Result is : {num_1/num_2}")
elif operator == '%':
    print(f"the Result is : {num_1%num_2}")
else:
    print("ERROR INPUT NUMBERS !! ")
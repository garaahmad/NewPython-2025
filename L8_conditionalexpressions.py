#check if the number is positive OR Negative
num = -5
print('positive' if num > 0 else 'Negative')

#check if the number is Even OR Odd
num = 6
result = "EVEN" if num%2 == 0 else "ODD"
print(result)

#return max number
a = 10
b = 5
max_num = a if a > b else b
min_num = a if a < b else b
print(max_num)

user_role ='admin'
access_level = 'Full Access' if user_role == 'admin' else "Limited Access"
print(access_level)
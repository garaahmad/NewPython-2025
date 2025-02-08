name = input('Enter your full name: ')
phone_number = input('Enter your phone number: ')
#To find  how many character  >> len()>>return integer
print(len(name))

#-----------------
#return the first occurrence of a given not found return -1
print(name.find('A'))

#return the last occurrence of a given if not found return -1
print(name.rfind('b'))

#Return a capitalized version of the string.only the first character
print(name.capitalize())

#Return a copy of the string converted to uppercase
print(name.upper())

#Return a copy of the string converted to lowercase.
print(name.lower())

#Return True if the string is a digit string, False otherwise
print(name.isdigit())

#Return True if the string is an alphabetic string, False otherwise.
print(name.isalpha())

#Return number of character like is...
print(phone_number.count('-'))

#Return a copy with all occurrences of substring old replaced by new
print(phone_number.replace('-' , '#'))


print('_'*50)

print('___ Validate user input exercise______')
userinput = input('Enter the Username: ')

if len(userinput) > 12 or not userinput.find(' ') or not userinput.isalpha():
    print('ERROR INPUT !!!')
else:
    print(f'Your Username is Validate ,Welcome {userinput}')
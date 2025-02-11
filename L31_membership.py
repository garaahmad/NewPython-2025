word = 'Apple'
letter = input('Guess a letter in secret word: ')

if letter in word:
    print(f'Threr is a {letter}')
else:
    print(f'{letter} was not found')
    
#by not in

if letter not in word:
    print(f'{letter} was not found')
else:
    print(f'Threr is a {letter}')
    
#_____________________
students ={'Ahmad' , 'Ali' , 'Omer'}
student = input('Enter the name of a student: ')
if student in students:
    print(f'{student} is a student')
else:
    print(f'{student} isnt a student')
    
#by not in
if student not in students:
    print(f'{student} isnt a student')
else:
    print(f'{student} is a student')
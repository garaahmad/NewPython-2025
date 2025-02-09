import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num  ,highest_num )
guesses = 0
is_running = True
print('Python Number Guessing Game')
print(f'Select a number between {lowest_num} and {highest_num}')


while is_running:
    guess = input('your Guess')
    if guess.isdigit():
        guess = int(guess)
        if guess <lowest_num or guess>highest_num:
            print('This is out of Reange')
            print(f'Select a number between {lowest_num} and {highest_num}')
        elif guess < answer:
            print('Too low !tey again!')
        elif guess > answer:
            print('Too high !tey again!')
        else:
            print(f'CORRECT! The answer was {answer}')
            print(f'The number of guesses : {guess}')
            is_running = False
            
            
    else:
        print('Invalid guess')
        print(f'Select a number between {lowest_num} and {highest_num}')
        
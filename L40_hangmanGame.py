import random


words = ('apple', 'orange' , 'banana' , 'coconut' , 'pineapple')

hangman = {0:("   ","   ","   "),
           1:(" o ","   ","   "),
           2:(" o "," | ","   "),
           3:(" o ","/| ","   "),
           4:(" o ","/|\\ ","   "),
           5:(" o ","/|\\","/   "),
           6:(" o ","/|\\","/ \\")}



def display_man(wrong_gusses):
    print('*'*10)
    for line in hangman[wrong_gusses]:
        print(line)
    print('*'*10)
    if wrong_gusses >= 6:
                print('Game Over')
                exit()
    

def display_hint(hint):
    print(" ".join(hint))
    

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint =["_"] * len(answer)
    wrong_gusses = 0
    gussed_letter = set()
    is_running = True
    while is_running:
        display_man(wrong_gusses)
        display_hint(hint)
        guess = input('Enter The Guess : ').lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print('invalid Input')
            continue
        
        if guess in gussed_letter:
            print(f'{guess} is guessed!')
            continue
        gussed_letter.add(guess)
        
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_gusses += 1
        
        if "_" not in hint:
            display_man(wrong_gusses)
            display_answer(answer)
            print('You WIN !')
            is_running = False
if __name__ == '__main__':
    main()
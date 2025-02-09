import random

low = 1
high = 100
options = ('rock' , 'paper' , 'scissors')
cards = ['2','2','6','4','8','9','6','9','g','x','d']
#return integer number of spacefic range
number = random.randint(low,high)
print(number)

#return integer number of 0 >> 1
number = random.random()

#Choose a random element from a non-empty sequence.
option = random.choice(options)
print(option)

#Shuffle list x in place, and return None.
random.shuffle(cards)
print(cards)
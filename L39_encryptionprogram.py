import random
import string

chars = " " + string.whitespace + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
keys = chars.copy()

random.shuffle(keys)
# print(f"The chars is :{chars}")
# print(f"The keys is :{keys}")

cipher_text = ''

plain_text = input('Enter a message to encrypt: ')
for letter in plain_text:
    index = chars.index(letter)
    cipher_text += keys[index]
print(f'Your message is : {plain_text}')
print(f'The encrypt message is : {cipher_text}')


plain_text =''
cipher_text = input('Enter a message to encrypt: ')
for litter in cipher_text:
    index = keys.index(litter)
    plain_text += chars[index]
print(f'The encrypt message is : {cipher_text}')
print(f'Your message is : {plain_text}')

    

        


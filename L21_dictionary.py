capital = {'USA':'Washington D.C','India':'New Delhi','China':'Beijing','Russia':'Moscow'}

#If find the Key Return Value
print(capital.get('USA'))
print(capital.get('India'))
print(capital.get('Japan'))

if capital.get('Japan'):
    print('The capital is exists')
else:
    print('The capital ist\'n exists')
    

#insert new Elements
capital.update({'Germany':'Berlin'})

#return Keys
print(capital.keys())

#return Values
print(capital.values())

#retuen all item(key and value)
print(capital.items())

#remove element by Key
capital.pop('India')
print(capital)

#remove last Element
capital.popitem()

#remove all Element
capital.clear()

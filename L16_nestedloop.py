for x in range(3):
    for y in range(1,10):
        print(y,end="-")
    print('\n')
    
    
#rectangel

rows = int(input('Enter the # of rows: '))
columns = int(input('Enter the # of Columns: '))
symbol = input('Enter a symbol to use: ')

for x in range(rows):
    for y in range(columns):
        print(symbol,end='')
    print()
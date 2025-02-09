for x in range(1,10):#Start >> end
    print(x)

print('_'*50)

for x in reversed (range(1,10)):# end >> Start
    print(x)
    
print('_'*50)

for x in reversed (range(1,10,2)):# end >> Start and step(Count by step)
    print(x)
    
credit_card = "1234-5678-9123-4567"
for x in credit_card:
    print(x)
    
for x in range(1,21):
    if x == 13:
        continue
    else:
        print(x)
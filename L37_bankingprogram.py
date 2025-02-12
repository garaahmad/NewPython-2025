def show_balance(balance):
    print(f'Your balance is ${balance:.2f}')

def deposit():
    amount = float(input('Enter an amount to be deposited: '))
    if amount < 0:
        print('That is not valid amount')
        return 0
    else:
        return amount        

def withdraw(balance):
    amount = float(input('Enter an amount to be withdrawn: '))
    if amount > balance:
        print('Insufficient Funds')
        return 0
    elif amount < 0:
        print('amount must by grater than 0')
        return 0
    else:
        return amount
    
def main():
    balance = 0
    is_running = True

    while is_running:
        print('*' *30)
        print('       Binking Program')
        print('*' *30)
        print("1. Show balance")
        print('2. Deposit')
        print('3. Withdraw')
        print('4. Exit')
        
        choice = input('Enter your Choice  (1-4): ')
        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print('That is not valid Choice')
    print('Thank You Have Nice Day')
    
main()
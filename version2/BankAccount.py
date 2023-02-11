"""List of operations for bank account simulation"""
"""
version 2:
Single account with functions

"""

accountName = ''
accountBalance = 0
accountPassword = ''

def newAccount(name, balance, password):
    global accountName, accountBalance, accountPassword
    accountName = name
    accountBalance = balance
    accountPassword = password

def show():
    global accountName, accountBalance, accountPassword
    print(' Name ', accountName)
    print(' Balance ', accountBalance)
    print(' Password ', accountPassword)
    print()

def getBalance(password):
    global accountBalance, accountName, accountPassword
    if password != accountPassword:
        print('Incorrect Password!')
        return None
    else:
        return accountBalance

def deposit(password, amountToDeposit):
    global accountName, accountBalance, accountPassword
    if amountToDeposit <= 0:
        print('Please enter amount greater than zero')
        return None

    if password != accountPassword:
        print('Incorrect Password')
        return None

    accountBalance += amountToDeposit
    return accountBalance

def withdraw(password, amountToWithdraw):
    global accountName, accountBalance, accountPassword
    if amountToWithdraw > accountBalance:
        print('You cannot withdraw more than your currenct balance')
        return None

    if amountToWithdraw <= 0:
        print('You cannot withdraw less than or equal to zero ')
        return None

    if password != accountPassword:
        print('Incorrect password')
        return None
    accountBalance -= amountToWithdraw
    return accountBalance
#create an account first
newAccount("Harry",2000, 'apple')
while True:
    print()
    print('press b to get the balance')
    print('press d to make a deposit')
    print('press w to make a withdraw')
    print('press s to show the account balance')
    print('press q to quit')
    print()

    action = input('What do you want to do? ')
    action = action.lower()
    action = action[0]
    print()

    if action == 'b':
        print('Get balance: ')
        userPassword = input('Please enter the password: ')
        theBalance = getBalance(userPassword)

        if theBalance is not None:
            print('Your account balance is : ', accountBalance)
    
    elif action == 'd':
        print('Deposit :')
        userDepositAmount = input('Please enter amount to deposit ')
        userDepositAmount = int(userDepositAmount)
        userPassword = input('Please enter the password ')
        theBalance = deposit(userPassword, userDepositAmount)
        if theBalance is not None:
            print('Your new balance is: ', accountBalance)
            
    elif action == 'w':
        print('Withdraw ')
        userWithDrawAmount = input('Please enter amount that you want to withdraw ')
        userWithDrawAmount =int (userWithDrawAmount)
        userPassword = input('Please enter the password ')
        theBalance = withdraw(userPassword, userWithDrawAmount)
        if theBalance is not None:
            print('Your new account balance is ', accountBalance) 
    elif action == 's':
        print('Show balance')
        userPassword = input('Please enter your password ')
        if userPassword != accountPassword:
            print('Incorrect password')
        else:
            show()
    elif action == 'q':
        break
print('Done')
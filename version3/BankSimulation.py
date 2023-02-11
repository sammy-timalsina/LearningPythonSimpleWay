"""List of operations for bank account simulation"""
"""
version 2:
Single account with functions

"""

accountNameList = []
accountBalanceList = []
accountPasswordList = []

def newAccount(name, balance, password):
    global accountNameList, accountBalanceList, accountPasswordList
    accountNameList.append(name)
    accountBalanceList.append(balance)
    accountPasswordList.append(password)

def show(accountNumber):
    global accountNameList, accountBalanceList, accountPasswordList
    print(' Name ', accountNameList[accountNumber])
    print(' Balance ', accountBalanceList[accountNumber])
    print(' Password ', accountPasswordList[accountNumber])
    print()

def getBalance(password,accountNumber):
    global accountBalanceList, accountNameList, accountPasswordList
    if password != accountPasswordList[accountNumber]:
        print('Incorrect Password!')
        return None
    else:
        return accountBalanceList[accountNumber]

def deposit(password, accountNumber ,amountToDeposit):
    global accountNameList, accountBalanceList, accountPasswordList
    if amountToDeposit <= 0:
        print('Please enter amount greater than zero')
        return None

    if password != accountPasswordList[accountNumber]:
        print('Incorrect Password')
        return None

    accountBalanceList[accountNumber] += amountToDeposit
    return accountBalanceList[accountNumber]

def withdraw(password, accountNumber, amountToWithdraw):
    global accountNameList, accountBalanceList, accountPasswordList
    if amountToWithdraw > accountBalanceList[accountNumber]:
        print('You cannot withdraw more than your currenct balance')
        return None

    if amountToWithdraw <= 0:
        print('You cannot withdraw less than or equal to zero ')
        return None

    if password != accountPasswordList[accountNumber]:
        print('Incorrect password')
        return None
    accountBalanceList[accountNumber] -= amountToWithdraw
    return accountBalanceList
#create an account first
newAccount("Harry",2000, 'apple')
newAccount("Sam",200000, 'toy')
newAccount("Jackie",4588,'pot')
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
        userAccountNumber = input('Please enter your account number')
        userAccountNumber = int (userAccountNumber)
        userPassword = input('Please enter the password: ')
        theBalance = getBalance(userPassword, userAccountNumber)

        if theBalance is not None:
            print('Your account balance is : ', accountBalanceList[userAccountNumber])
    
    elif action == 'd':
        print('Deposit :')
        userAccountNumber = input('Please enter your account number')
        userAccountNumber = int (userAccountNumber)
        userDepositAmount = input('Please enter amount to deposit ')
        userDepositAmount = int(userDepositAmount)
        userPassword = input('Please enter the password ')
        theBalance = deposit(userPassword,userAccountNumber ,userDepositAmount)
        if theBalance is not None:
            print('Your new balance is: ', accountBalanceList[userAccountNumber])
            
    elif action == 'w':
        print('Withdraw ')
        userAccountNumber = input('Please enter your account number')
        userAccountNumber = int (userAccountNumber)
        userWithDrawAmount = input('Please enter amount that you want to withdraw ')
        userWithDrawAmount =int (userWithDrawAmount)
        userPassword = input('Please enter the password ')
        theBalance = withdraw(userPassword, userAccountNumber, userWithDrawAmount)
        if theBalance is not None:
            print('Your new account balance is ', accountBalanceList[userAccountNumber]) 
    elif action == 's':
        print('Show balance')
        userAccountNumber = input('Please enter your account number ')
        userAccountNumber = int (userAccountNumber)
        userPassword = input('Please enter your password ')
        if userPassword != accountPasswordList[userAccountNumber]:
            print('Incorrect password')
        else:
            show(userAccountNumber)
    elif action == 'q':
        break
print('Done')
"""List of operations for bank account simulation"""
"""
-create an account
-deposit
-withdraw 
-check balance

minimal list of the data that needs to represent a bank account

-customer name
-password
-balance

version1
"""

accountName = 'Sam'
accountBalance = 1000
accountPassword = 'soup'

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
        if userPassword != accountPassword:
            print('Incorrect password')
        else:
            print('Your account balance is : ', accountBalance)
    
    elif action == 'd':
        print('Deposit :')
        userDepositAmount = input('Please enter amount to deposit ')
        userDepositAmount = int(userDepositAmount)
        userPassword = input('Please enter the password ')

        if userDepositAmount <= 0:
           print('You cannot deposit amount less than zero. ')
        elif userPassword != accountPassword:
            print('Incorrect password')
        else:
            accountBalance += userDepositAmount
            print('Your new balance is: ', accountBalance)
            
    elif action == 'w':
        print('Withdraw ')
        userWithDrawAmount = input('Please enter amount that you want to withdraw ')
        userWithDrawAmount =int (userWithDrawAmount)
        userPassword = input('Please enter the password ')

        if userWithDrawAmount > accountBalance:
            print('You cannot withdraw more than your current balance ')
        elif userWithDrawAmount <= 0:
            print('You cannot withdraw less than or equal to zero. ')
        elif userPassword != accountPassword:
            print('Incorrect password')
        else:
            accountBalance -= userWithDrawAmount
            print('Your new account balance is ', accountBalance) 
    elif action == 's':
        print('Show balance')
        userPassword = input('Please enter your password ')
        if userPassword != accountPassword:
            print('Incorrect password')
        else:
            print('Account name ', accountName)
            print('Account Password', accountPassword)
            print('Your current balance is ', accountBalance)
    elif action == 'q':
        break
print('Done')



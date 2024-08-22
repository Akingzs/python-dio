# Simple Bank system

# Features
# - Withdraw
# - bank statement
# - Deposit


account_balance = 0
withdraw_value_limit = 3
withdraw_money_limit = 500.0
withdraw_count = 0
statement_history = []

while True:
    action = input('Please select an operation:\n (a) - Withdraw\n (b) - Bank Statement\n (c) - Deposit\n (d) - Exit\n')

    if  action.upper() == 'D':
        break
    # Withdraw action
    elif action.upper() == 'A':
        withdraw_action = float(input('How much do you want to withdraw: \n'))
        if withdraw_action > account_balance:
            print(f"You don't have enough balance to withdraw, your current balance is: {account_balance}\n")   
        elif  withdraw_count == 3:
            print('You have reached the daily withdraw limit ')
        elif withdraw_action > 500:
            print('OPERATION FAILED\nThe withdraw limit is $500\n')
        else:
            statement_history.append(f'-${withdraw_action}')
            withdraw_count += 1
    
    #Bank Statement           
    elif action.upper() == 'B':
        print('Bank Statement')
        if len(statement_history) == 0:
            print('No transactions to show')
        for action in statement_history:
            print(f'{action}',end='\n')
    
    #Deposit action 
    elif action.upper() == 'C':
        deposit_action = float(input('How much do you want to deposit: '))
        account_balance += deposit_action
        statement_history.append(f'+${deposit_action}')


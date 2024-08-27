# Simple Bank system

# Features
# - Withdraw
# - bank statement
# - Deposit

def withdraw(*, cpf, value, withdraw_limit, withdraw_count):

    return statement

def deposit(cpf, account_nb, value, /):
    deposit_validation = user_validation(cpf)
    account_validation_ = account_validation(account_nb)
    # If cpf is already in database
    if not deposit_validation and account_validation_:
        print(f'Deposit value: {value}\n')
        user_filtered = [account for account in accounts if account['user'] == cpf]

        user_filtered[0]['balance'] += value

        print(user_filtered)


    return 



def statement(balance, /,*,statement):

    return statement

def user_validation(cpf):
    for user in users:
        if user['cpf'] == cpf:
            # False means I can't create new user
            return False
    # True means I can create new user
    return True

def account_validation(account_nb):
    for account in accounts:
        if account['account_nb'] == int(account_nb):
            # Account exists
            return True
    # Account doesn't exists
    return False

def new_user():
    cpf = str(input('Enter your CPF. Only numbers!'))
    if len(cpf) == 10:
        # Check if user already exists
        validation = user_validation(cpf)
        if validation:
            name = str(input('Name: '))
            address = str(input('address: '))
            birth_date = str(input('birth_date: '))
            # Adding new user to list
            users.append({'cpf': cpf,
                           'name': name,
                           'birth_date': birth_date,
                           'address': address})
        else:
            print("You can't create a new user. Your CPF already is in our database ")

def new_account(cpf, balance = 0.0, withdraw_count = 0):
    validation_acount = user_validation(cpf)
    if not validation_acount:
        global account_creation_iterator

        account_creation_iterator += 1

        accounts.append({'user': cpf,
                        'agency': '0001',
                        'account_nb': account_creation_iterator,
                        'balance': balance,
                        'withdraw_count': withdraw_count
                        })
        print(f'Account: {account_creation_iterator} | agency: 0001, created for the CPF: {cpf}')

        
    else: 
        print('Cannot create account')

accounts = []
users = []
account_balance = 0
withdraw_value_limit = 3
withdraw_money_limit = 500.0
withdraw_count = 0
statement_history = []
account_creation_iterator = 0

while True:
    a = input('Select an option: ')

    if a == '1':
        new_user()
    elif a == '2':
        cpf = input('Enter CPF: ')
        new_account(cpf)
    elif a == '3':
        cpf = input('Enter CPF: ')
        account_nb = input('Number account: ')
        deposit_value = float(input('Deposit value: '))
        deposit(cpf,account_nb,deposit_value)
    elif a == '9':
        break

# while True:
#     action = input('Please select an operation:\n (a) - Withdraw\n (b) - Bank Statement\n (c) - Deposit\n (d) - Exit\n')

#     if  action.upper() == 'D':
#         break
#     # Withdraw action
#     elif action.upper() == 'A':
#         withdraw_action = float(input('How much do you want to withdraw: \n'))
#         if withdraw_action > account_balance:
#             print(f"You don't have enough balance to withdraw, your current balance is: {account_balance}\n")   
#         elif  withdraw_count == 3:
#             print('You have reached the daily withdraw limit ')
#         elif withdraw_action > 500:
#             print('OPERATION FAILED\nThe withdraw limit is $500\n')
#         else:
#             statement_history.append(f'-${withdraw_action}')
#             withdraw_count += 1
    
#     #Bank Statement           
#     elif action.upper() == 'B':
#         print('Bank Statement')
#         if len(statement_history) == 0:
#             print('No transactions to show')
#         for action in statement_history:
#             print(f'{action}',end='\n')
    
#     #Deposit action 
#     elif action.upper() == 'C':
#         deposit_action = float(input('How much do you want to deposit: '))
#         account_balance += deposit_action
#         statement_history.append(f'+${deposit_action}')


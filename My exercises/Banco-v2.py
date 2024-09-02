# Bank using function 

import os
# Features
# - Create users
# - Create accounts for users  
# - Withdraw
# - bank statement
# - Deposit

# Function to clear the console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def withdraw(*, cpf, account_nb, withdraw_value, withdraw_limit = 500.0):
    """
    Performs a withdrawal from a bank account.

    Parameters:
    - cpf (str): User's CPF.
    - account_nb (str): Bank account number.
    - withdraw_value (float): Amount to withdraw.
    - withdraw_limit (float): Daily withdrawal limit, default is $500. Optional in my code version

    Returns:
    - None
    """
    withdraw_validation = user_validation(cpf)
    account_validation_ = account_validation(account_nb)

    # CPF and acc number check
    if withdraw_validation:
        show_error_message('Invalid CPF')
        return None
    if not account_validation_:
        show_error_message('Invalid account number')
        return None

    if withdraw_validation and account_validation_:
        user_filtered = [account for account in accounts if account['user'] == cpf and account['account_nb'] == account_nb]
        
        # Ensure that a matching account was found
        if user_filtered:
            user_filtered[0]['balance'] += withdraw_value
            user_filtered[0]['account_statement'].append(f'+ ${withdraw_value}')
            print('#### OPERATION COMPLETED SUCCESSFULLY ####\n')
        else:
            show_error_message('CPF and account number do not match')

        if not user_filtered:
            show_error_message('User account not found')
            return None

        withdraw_count = user_filtered[0]['withdraw_count']

        # Check Balance
        if user_filtered[0]['balance'] < withdraw_value:
            show_error_message('Insufficient balance')
            return None
        # Daily limit and withdraw value check
        if withdraw_count <= 3 and withdraw_value <= withdraw_limit:
            user_filtered[0]['balance'] -= withdraw_value
            user_filtered[0]['withdraw_count'] += 1
            user_filtered[0]['account_statement'].append(f'- ${withdraw_value}')
            print('#### OPERATION COMPLETED SUCCESSFULLY ####')

    elif withdraw_value > 500.0:
       show_error_message('Withdraw value above $500')
    elif withdraw_count > 3:
        show_error_message('#### OPERATION DAILY LIMIT REACHED ####\n')

    return None

def show_error_message(message):
 print(f'#### OPERATION ERROR ####\n{message}')

def deposit(cpf, account_nb, value, /):
    """
    Performs a withdrawal from a bank account.

    Parameters:
    - cpf (str): User's CPF.
    - account_nb (str): Bank account number.
    - withdraw_value (float): Amount to withdraw.
    - withdraw_limit (float): Daily withdrawal limit, default is $500. Optional in my code version

    Returns:
    - None
    """
    
    deposit_validation = user_validation(cpf)
    account_validation_ = account_validation(account_nb)

    # Check if both CPF and account number are valid and belong to the same user
    if deposit_validation and account_validation_:
        user_filtered = [account for account in accounts if account['user'] == cpf and account['account_nb'] == account_nb]
        
        # Ensure that a matching account was found
        if user_filtered:
            user_filtered[0]['balance'] += value
            user_filtered[0]['account_statement'].append(f'+ ${value}')
            print('#### OPERATION COMPLETED SUCCESSFULLY ####\n')
        else:
            show_error_message('CPF and account number do not match')
    else:
        if not deposit_validation:
            show_error_message('Invalid CPF')
        elif not account_validation_:
            show_error_message('Invalid account number')

    return None


def statement(cpf ,account_nb,/):
    withdraw_validation = user_validation(cpf)
    account_validation_ = account_validation(account_nb)

    if not withdraw_validation and account_validation_: 
        user_filtered = [account for account in accounts if account['user'] == cpf]
        print(user_filtered[0]['account_statement'])


    return 

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
    cpf = str(input('Enter your CPF. Only numbers!\n'))
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
            print('#### OPERATION COMPLETED SUCCESSFULLY ####\n')
        else:
           show_error_message("You can't create a new user. Your CPF already is in our database")

def new_account(cpf, balance = 0.0, withdraw_count = 0, /):
    validation_acount = user_validation(cpf)
    if not validation_acount:
        global account_creation_iterator

        account_creation_iterator += 1

        accounts.append({'user': cpf,
                        'agency': '0001',
                        'account_nb': account_creation_iterator,
                        'balance': balance,
                        'withdraw_count': withdraw_count,
                        'account_statement': []
                        })
        print('#### OPERATION COMPLETED SUCCESSFULLY ####')
        print(f'Account: {account_creation_iterator} | agency: 0001, created for the CPF: {cpf}\n')

        
    else: 
        show_error_message('Cannot create account')

def show_user():
    print(users)

def show_acc():
    print(accounts)

accounts = []
users = []
account_balance = 0
withdraw_value_limit = 3
withdraw_money_limit = 500.0
withdraw_count = 0
statement_history = []
account_creation_iterator = 0

while True:
    # Input selection
    a = input('Select an option:\n1 - Create new user\n2 - Create new account\n3 - Deposit\n4 - Withdraw\n5 - Bank Statement\n9 - Exit\n')

    if a == '1':
        # Clear the console
        clear_console()
        new_user()
    elif a == '2':
        # Clear the console
        clear_console()
        cpf = input('Enter CPF: ')
        new_account(cpf)
    elif a == '3':
        # Clear the console
        clear_console()
        cpf = input('Enter CPF: ')
        account_nb = input('Number account: ')
        deposit_value = float(input('Deposit value: '))
        deposit(cpf,account_nb,deposit_value)
    elif a == '4':
        # Clear the console
        clear_console()
        cpf = input('Enter CPF: ')
        account_nb = input('Number account: ')
        withdraw_value = float(input('Withdraw value: '))
        withdraw(cpf = cpf,account_nb = account_nb , withdraw_value = withdraw_value)
    elif a == '5':
        # Clear the console
        clear_console()
        cpf = input('Enter CPF: ')
        account_nb = input('Number account: ')
        statement(cpf = cpf,account_nb = account_nb)
    elif a == '6':
        # Clear the console
        clear_console()
        show_acc()
        show_user()

    elif a == '9':
        break



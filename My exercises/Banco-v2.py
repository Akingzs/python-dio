# Bank using function 

# Features
# - Create users
# - Create accounts for users  
# - Withdraw
# - bank statement
# - Deposit

def withdraw(*, cpf, account_nb, withdraw_value, withdraw_limit = 500.0):
    withdraw_validation = user_validation(cpf)
    account_validation_ = account_validation(account_nb)
    # If cpf is already in database
    if not withdraw_validation and account_validation_: 
        print(f'Withdraw value: {withdraw_value}\n')
        user_filtered = [account for account in accounts if account['user'] == cpf]
        withdraw_count = user_filtered[0]['withdraw_count']

        if withdraw_count <= 3 and withdraw_value <= withdraw_limit:
            user_filtered[0]['balance'] -= withdraw_value
            user_filtered[0]['withdraw_count'] += 1
            user_filtered[0]['account_statement'].append(f'- ${withdraw_value}')
            print('#### OPERATION COMPLETED SUCCESSFULLY ####')

    elif withdraw_value > 500.0:
        print('#### OPERATION ERRROR ####\nWithdraw value above $500')
    elif withdraw_count <= 3:
        print('#### OPERATION ERRROR ####\n')
        print('#### OPERATION DAILY LIMIT REACHED ####\n')

    return None

def deposit(cpf, account_nb, value, /):
    deposit_validation = user_validation(cpf)
    account_validation_ = account_validation(account_nb)
    # If cpf is already in database
    if not deposit_validation and account_validation_:
        print(f'Deposit value: {value}\n')
        user_filtered = [account for account in accounts if account['user'] == cpf]
        user_filtered[0]['balance'] += value
        user_filtered[0]['account_statement'].append(f'+ ${value}')

        print('#### OPERATION COMPLETED SUCCESSFULLY ####\n')
    else:
        print('#### OPERATION ERRROR ####\n')
    return None

def statement(cpf ,account_nb):
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
            print('#### OPERATION ERROR ####\n')
            print("You can't create a new user. Your CPF already is in our database ")

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
    a = input('Select an option:\n1 - Create new user\n2 - Create new account\n3 - Deposit\n4 - Withdraw\n5 - Bank Statement\n9 - Exit\n')

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
    elif a == '4':
        cpf = input('Enter CPF: ')
        account_nb = input('Number account: ')
        withdraw_value = float(input('Withdraw value: '))
        withdraw(cpf = cpf,account_nb = account_nb , withdraw_value = withdraw_value)
    elif a == '5':
        cpf = input('Enter CPF: ')
        account_nb = input('Number account: ')
        statement(cpf = cpf,account_nb = account_nb)

    elif a == '9':
        break



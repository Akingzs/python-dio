import datetime
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

    if not withdraw_validation and account_validation_:
        user_filtered = [account for account in accounts if account['user'] == cpf and account['account_nb'] == account_nb]
        
        # Ensure that a matching account was found
        if user_filtered:

            withdraw_count = user_filtered[0]['withdraw_count']

            # Daily limit and withdraw value check
            if withdraw_count < 3 and withdraw_value <= withdraw_limit:
                user_filtered[0]['balance'] -= withdraw_value
                user_filtered[0]['withdraw_count'] += 1
                user_filtered[0]['account_statement'].append(f'- ${withdraw_value} -- {datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M:%S")}')
                print('#### OPERATION COMPLETED SUCCESSFULLY ####')
            
            # Check Balance
            elif user_filtered[0]['balance'] < withdraw_value:
                show_error_message('Insufficient balance')
                return None

            elif withdraw_value > 500.0:
                show_error_message('Withdraw value above $500')

            elif withdraw_count > 3:
                show_error_message('#### OPERATION DAILY LIMIT REACHED ####\n')
                
            else:
                show_error_message('CPF and account number do not match')

        if not user_filtered:
            show_error_message('User account not found')
            return None
        

    return None


def show_error_message(message):
 print(f'#### OPERATION ERROR ####\n{message}')

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


users = []
accounts = []
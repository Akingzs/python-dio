import unittest
from unittest.mock import patch
from bank_code import withdraw, accounts, user_validation, account_validation, show_error_message

class TestWithdraw(unittest.TestCase):

    def setUp(self):
        # Setting up initial state for accounts
        accounts.clear()
        accounts.append({
            'user': '1234567890',
            'account_nb': '987654321',
            'balance': 1000.0,
            'withdraw_count': 0,
            'account_statement': []
        })

    @patch('bank_code.user_validation', return_value=False)
    @patch('bank_code.account_validation', return_value=True)
    @patch('bank_code.show_error_message')
    def test_withdraw_success(self, mock_error_message, mock_account_validation, mock_user_validation):
        withdraw(cpf='1234567890', account_nb='987654321', withdraw_value=200.0)

        # Check that the balance was updated correctly
        self.assertEqual(accounts[0]['balance'], 800.0)
        self.assertEqual(accounts[0]['withdraw_count'], 1)
        self.assertEqual(len(accounts[0]['account_statement']), 1)
        self.assertIn('- $200.0', accounts[0]['account_statement'][0])

        # Ensure no error message was shown
        mock_error_message.assert_not_called()

    @patch('bank_code.user_validation', return_value=True)
    @patch('bank_code.account_validation', return_value=True)
    @patch('bank_code.show_error_message')
    def test_invalid_cpf(self, mock_error_message, mock_account_validation, mock_user_validation):
        withdraw(cpf='invalid_cpf', account_nb='987654321', withdraw_value=200.0)

        # Ensure no changes to balance
        self.assertEqual(accounts[0]['balance'], 1000.0)

        # Check that the correct error message was shown
        mock_error_message.assert_called_once_with('Invalid CPF')

    @patch('bank_code.user_validation', return_value=False)
    @patch('bank_code.account_validation', return_value=False)
    @patch('bank_code.show_error_message')
    def test_invalid_account_number(self, mock_error_message, mock_account_validation, mock_user_validation):
        withdraw(cpf='1234567890', account_nb='invalid_account', withdraw_value=200.0)

        # Ensure no changes to balance
        self.assertEqual(accounts[0]['balance'], 1000.0)

        # Check that the correct error message was shown
        mock_error_message.assert_called_once_with('Invalid account number')

    @patch('bank_code.user_validation', return_value=False)
    @patch('bank_code.account_validation', return_value=True)
    @patch('bank_code.show_error_message')
    def test_insufficient_balance(self, mock_error_message, mock_account_validation, mock_user_validation):
        withdraw(cpf='1234567890', account_nb='987654321', withdraw_value=1200.0)

        # Ensure no changes to balance
        self.assertEqual(accounts[0]['balance'], 1000.0)

        # Check that the correct error message was shown
        mock_error_message.assert_called_once_with('Insufficient balance')

    @patch('bank_code.user_validation', return_value=False)
    @patch('bank_code.account_validation', return_value=True)
    @patch('bank_code.show_error_message')
    def test_exceed_withdraw_limit(self, mock_error_message, mock_account_validation, mock_user_validation):
        withdraw(cpf='1234567890', account_nb='987654321', withdraw_value=600.0)

        # Ensure no changes to balance
        self.assertEqual(accounts[0]['balance'], 1000.0)

        # Check that the correct error message was shown
        mock_error_message.assert_called_once_with('Withdraw value above $500')

    @patch('bank_code.user_validation', return_value=False)
    @patch('bank_code.account_validation', return_value=True)
    @patch('bank_code.show_error_message')
    def test_exceed_daily_withdraw_limit(self, mock_error_message, mock_account_validation, mock_user_validation):
        accounts[0]['withdraw_count'] = 4
        withdraw(cpf='1234567890', account_nb='987654321', withdraw_value=200.0)

        # Ensure no changes to balance
        self.assertEqual(accounts[0]['balance'], 1000.0)

        # Check that the correct error message was shown
        mock_error_message.assert_called_once_with('#### OPERATION DAILY LIMIT REACHED ####\n')

if __name__ == '__main__':
    unittest.main()

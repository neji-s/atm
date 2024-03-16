import unittest
from atm_sim import ATM

class TestATM(unittest.TestCase):
    def test_deposit(self):
        # Normal case
        # Arrange
        atm = ATM(balance=1000)
        deposit_amount = 250
        expected_balance = 1250
        # Act
        atm.deposit(deposit_amount)
        true_balance = atm.balance
        # Assert
        self.assertEqual(true_balance, expected_balance, 'Incorrect balance. Deposit test failed')
        
        # Edge case: Deposit 10x balance
        # Arrange
        atm = ATM(balance=1000)
        deposit_amount = 10000
        expected_balance = 11000
        # Act
        atm.deposit(deposit_amount)
        true_balance = atm.balance
        # Assert
        self.assertEqual(true_balance, expected_balance, 'Incorrect balance. Deposit edge case test failed')
        
        # Corner case: Deposit nothing
        # Arrange
        atm = ATM(balance=1000)
        deposit_amount = 0
        expected_balance = 1000
        # Act
        atm.deposit(deposit_amount)
        true_balance = atm.balance
        # Assert
        self.assertEqual(true_balance, expected_balance, 'Incorrect balance. Deposit corner case test failed')

    
    def test_withdraw(self):
        # Normal case
        # Arrange
        atm = ATM(balance=1000)
        withdrawal_amount = 300
        expected_balance = 700
        # Act
        atm.withdraw(withdrawal_amount)
        true_balance = atm.balance
        # Assert
        self.assertEqual(true_balance, expected_balance, 'Incorrect balance. Withdrawal test failed')
        
        # Edge case: withdrawing entire balance
        # Arrange
        atm = ATM(balance=1000)
        withdrawal_amount = 1000
        expected_balance = 0
        # Act
        atm.withdraw(withdrawal_amount)
        true_balance = atm.balance
        # Assert
        self.assertEqual(true_balance, expected_balance, 'Incorrect balance. Withdrawal edge case test failed')
        
        # Corner case: withdrawing nothing
        # Arrange
        atm = ATM(balance=1000)
        withdrawal_amount = 0
        expected_balance = 1000
        # Act
        atm.withdraw(withdrawal_amount)
        true_balance = atm.balance
        # Assert
        self.assertEqual(true_balance, expected_balance, 'Incorrect balance. Withdrawal corner case test failed')
        
if __name__ == '__main__':
    unittest.main()
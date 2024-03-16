import requests

class ATM:
    def __init__(self, balance=1000):
        self.balance = balance
        
    def deposit(self, deposit_amount):
        self.balance += deposit_amount
    
    def withdraw(self, withdraw_amount):
        if withdraw_amount <= self.balance:
            self.balance -= withdraw_amount
        else:
            print(f'Insufficient funds. You can withdraw a maximum of £{self.balance}')
    
    def view_balance(self):
        return print(f'Your current balance is £{self.balance}')
    
    def get_exchange_rate(self, base_currency):
        api_url = f"https://api.exchangeratesapi.io/latest?base={base_currency}"
        try:
            response = requests.get(api_url)
            data = response.json()
                
            if response.status_code == 200:
                gbp_to_usd = data['rates']['USD']
                return gbp_to_usd
            
            else:
                print(f"Error: {data['error']}")
                return None
            
        except Exception as e:
                print(f"Error: {e}")
                return None


def welcome_message():
    print('Welcome to Python Bank!')

def main_menu():
    print()
    print('1. Deposit Funds')
    print('2. Make a Withdrawal')
    print('3. Get Exchange Rate')
    print('4. View Balance')
    print('5. Exit')
    print()
    
def exit_message():
    print()
    print('Thank you for using Python Bank. Goodbye!')
    print()

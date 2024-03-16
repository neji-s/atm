from atm_sim import *

account = ATM()

welcome_message()

while True:
    main_menu()
    menu_option = input('Please select your menu option number: ')
    menu_option = menu_option.strip()
    
    if menu_option == '1':
        deposit_amount = int(input('Please enter how much you would like to deposit: £'))
        account.deposit(deposit_amount)
        account.view_balance()
    
    elif menu_option == '2':
        withdrawal_amount = int(input('Please enter how much you would like to withdraw: £'))
        account.withdraw(withdrawal_amount)
        account.view_balance()
    
    elif menu_option == '3':
        account.get_exchange_rate('GBP')
        
    elif menu_option == '4':
        account.view_balance()
    
    elif menu_option == '5':
        exit_message()
        break
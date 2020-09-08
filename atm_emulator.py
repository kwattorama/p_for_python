

# Welcome message
# Enter the card
# Language selection - English, Hindi,
# Enter Pin
# Verify Pin
# Show Menu - Withdraw, Chnage Pin, Check balance, Transfer, Deposite
#   Withdraw - Saving, Current
#       Saving - Enter Amount
#           Processing Prompt and collect cash message
# Print Receipt option - Y/N
# Exit transaction

import time
import random
from users import users

print('Welcome! to The Billionaires Piggy Bank\n')
while True:

    ins = input("press 'I' after inserting the card>>> ")
  
    if ins == "I" or ins == "i":
        languages = ["English", "Hindi"]

        for lang_idx, languages in enumerate(languages, start=1):
            print(f"{lang_idx}. {languages}")

        lang = int(input("Choose your language[1/2]>>> "))

        if lang == 2:
            print('This feature is coming soon...Until then ENGLISH would be set by default.')
            
        attempt = 1
        print(f"Processing...")

        while attempt <= 3:
            time.sleep(2)
            atm_pin = int(input('Enter your 4 digit ATM pin>>> '))

            if atm_pin in users:
                first_name = users[atm_pin]['first_name']
                last_name = users[atm_pin]['last_name']
                account_no = users[atm_pin]['account_no']
                balance = users[atm_pin]['balance']
                currency = users[atm_pin]['currency']
                print(
                    f'Hello {first_name} {last_name}, Your TBP Bank a/c no. is {account_no}\n')

                while True:
                    print('What would you like to do?')
                    options = ['Check Balance', 'Withdraw', 'Deposite', 'Transfer', 'Change the PIN', 'Exit']
                    for idx, option in enumerate(options, start=1):
                        print(f"{idx}. {option}")

                    task = int(input('\nChoose from above options>>> '))

                 
                    if task in [1, 2, 3, 4, 5, 6]:
                        if task == 1:
                            print('Please wait..Your account details are getting fetched..\n')
                            time.sleep(1.0)
                            print(f'Your TBP bank a/c balance is {currency}{balance}.\n')
                            time.sleep(2.0)
                        elif task == 2:
                            print('1. Saving Account\n2. Current Account')
                            acc_type_ip = input('Choose your account type>>>')
                            if acc_type_ip == '1':
                                withdraw = int(input('Enter the amount>>>'))
                                if withdraw > balance:
                                    print(
                                        'Withdraw amount is greater than your Account balance')
                                else:
                                    balance = balance - withdraw
                                    print(
                                        f"your account balance is {currency}{balance}")
                                    time.sleep(3.0)
                            elif acc_type_ip == '2':
                                print('You dont have Current account')
                            else:
                                print('Invalid Choice')
                                break
                        elif task == 3:
                            pass  #  Coming soon...
                        elif task == 4:
                            pass  #  Coming soon...
                        elif task == 5:
                                new_pin = int(input('Enter 4 digit NEW PIN>>>'))
                                new_pin = int(input('Please re-enter 4 digit NEW PIN>>>'))
                                if len(str(new_pin)) == 4:
                                    temp = users[atm_pin]
                                    
                                    del users[atm_pin]
                                    users[new_pin] = temp
                                    print(f"ATM pin updating.{time.sleep(0.5)}.{time.sleep(0.5)}.")
                                    time.sleep(2.0)
                                    print("Your pin has been change successfully")
                        elif task == 6:
                            print("Thank you for visiting...\nHave a nice day!")
                            break
                    else:
                        print("Invalid Choice. Try again...\n")
                break
            else:
                attempt += 1
                if attempt == 2:
                    print("Invalid ATM Pin. Only 2 attempts remaining...")
                elif attempt == 3:
                    print("Invalid ATM Pin. Only 1 attempt remaining...")
                else:
                    print("This ATM card has been BLOCKED for Security reasons.\nTBP will contact you soon.")     
        break
    else:
        print("Card not properly inserted! Try Again...")
        print("1. Continue\n2. Cancel")
        c = input("Enter your choice[1/2]>>> ")
        if c == "1":
            continue
        else:
            print("Thank you for visiting...\nHave a nice day!")
            break

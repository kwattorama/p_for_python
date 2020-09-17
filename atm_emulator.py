

# Welcome message
# Enter the card
# Language selection - English, Hindi
# Enter Pin
# Verify Pin
# Show Menu - Withdraw, Chnage Pin, Check balance, Transfer, Deposite
#   Withdraw - Saving, Current
#              Saving - Enter Amount
#              Processing Prompt and collect cash message
# Print Receipt option - Y/N
# Exit message

import time


from users import users

print("\nWelcome! to The Billionaires Piggy Bank\n")
while True:

    ins = input("press 'I' after inserting the card>>> ")
 
    
    if ins == "I" or ins == "i":
        languages = ["English", "Hindi"]

        for lang_idx, languages in enumerate(languages, start=1):
            print(f"{lang_idx}. {languages}")

        lang = int(input("Choose your language[1/2]>>> "))

        if lang == 2:
            print(
                "This feature is coming soon...Until then By default, its's set to English")
        elif lang != 1:
            print("Invalid Option. By default, its's set to English")

        attempt = 1
        print(f"Processing...")

        while attempt <= 3:
            time.sleep(2)
            atm_pin = int(input("\nEnter your 4 digit ATM pin>>> "))

            if atm_pin in users:
                first_name = users[atm_pin]["first_name"]
                last_name = users[atm_pin]["last_name"]
                account_no = users[atm_pin]["account_no"]
                balance = users[atm_pin]["balance"]
                currency = users[atm_pin]["currency"]
                print(
                    f"\nHello {first_name} {last_name}, Your TBP Bank a/c no. is {account_no}")

                while True:
                    print("\nWhat would you like to do?")
                    options = ["Check Balance", "Withdraw", "Deposit",
                               "Transfer", "Change the PIN", "Exit"]
                    
                    for idx, option in enumerate(options, start=1):
                        print(f"{idx}. {option}")

                    task = int(input("Choose from above options>>> "))

                    if task in [1, 2, 3, 4, 5, 6]:
                        
                        if task == 1:
                            print(
                                'Please wait..Your account details are getting fetched..')
                            time.sleep(1.0)
                            print(
                                f"\na/c number: {account_no}\nName: {first_name} {last_name}\nBalance: {currency}{balance}")
                            time.sleep(3.0)
                        elif task == 2:
                            print("1. Saving Account\n2. Current Account")
                            acc_type_ip = input('Choose your account type>>> ')

                            if acc_type_ip == '1':
                                withdraw = int(input('\nEnter the amount>>> $'))

                                if withdraw > balance:
                                    print(
                                        'Withdraw amount is greater than your Account balance')
                                else:
                                    balance = balance - withdraw
                                    print(
                                        f"\nPlease collect your cash...\nyour account balance is {currency}{balance}")
                                    time.sleep(3.0)

                            elif acc_type_ip == '2':
                                print('\nYou dont have Current account')
                                time.sleep(2.5)
                            else:
                                print('\nInvalid Choice')
                                time.sleep(2.5)
                               
                        elif task == 3:
                            print(f"Your transaction is being processed \nPlease wait...")
                            time.sleep(2.0)
                            print(
                                "\nOnly $2000, $500 and $200 notes are acceptable.\nYou can deposit upto $50000 only.")
                            cc_1 = input("1. Continue\n2. Cancel\nPress 1 or 2 >>> ")

                            if cc_1 == "1":
                                print("\nPlease insert your cash...\nEnter numbers of cash note>>>")
                                two_thousand = int(input("$2000 x "))
                                # https: // stackoverflow.com/a/36210179
                                print(f"\033[{len(str(two_thousand)) + 8}C\033[1A",  
                                    f"= {2000 * two_thousand}")
                                five_hundred = int(input("$500 x "))
                                print(f"\033[{len(str(five_hundred)) + 8}C\033[1A",
                                    f"= {500 * five_hundred}")
                                two_hundred = int(input("$200 x "))
                                print(f"\033[{len(str(two_hundred)) + 8}C\033[1A",
                                    f"= {200 * two_hundred}")
                                total = (2000 * two_thousand) +(500 * five_hundred) + (200 * two_hundred)

                                if total <= 50000:
                                    print(
                                        f"Please wait...\nvalidating cash...")
                                    print(f"\nTotal amount to be deposite: ${total}")
                                    cc_2 = input("1. Confirm\n2. Add more cash(this service is currently not available)\n3. Cancel\nPress 1 or 2 or 3 >>> ")

                                    if cc_2 == "1":
                                        balance = balance + total
                                        print(
                                            f"Transaction Complete.\nYour TBP a/c balance is {currency}{balance}")
                                    elif cc_2 == "2":
                                        pass
                                    else:
                                        pass
                                else:
                                    print(f"\nPlease remove your cash\nYou can deposit upto $50000 only.")
                        elif task == 4:
                            receiver = int(input("\nEnter the Account Number>>> "))
                            receiver_1 = int(input("Re enter the Account Number>>> "))
                            print("Please wait")
                            for pin in users:

                                if users[pin]["account_no"] == receiver:

                                    if receiver == receiver_1:
                                        receiver_money = int(input("Enter the amount>>> "))

                                        if receiver_money > 0.6 * users[pin]["balance"]:
                                            print("You can only transfer 60% of your TBP bank balance")
                                        else:
                                            users[pin]["balance"] = users[pin]["balance"] + receiver_money
                                            balance = balance - receiver_money
                                            print(
                                                f'Money Transfer to {users[pin]["first_name"]} {users[pin]["last_name"]} is successful.\na/c number : ******{str(users[pin]["account_no"])[6:]}\nSend amount: ${receiver_money}')
                                            print(f'Your account balance is {balance}')
                        elif task == 5:
                            new_pin=int(input('Enter 4 digit NEW PIN>>> '))
                            new_pin=int(
                                input('Please re-enter 4 digit NEW PIN>>> '))

                            if len(str(new_pin)) == 4:
                                temp=users[atm_pin]

                                del users[atm_pin]
                                users[new_pin]=temp
                                print(
                                    f"ATM pin updating.{time.sleep(0.5)}.{time.sleep(0.5)}.")
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
                    print(
                        f"This ATM card has been BLOCKED for Security reasons.\nTBP bank will contact this card holder soon.")
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

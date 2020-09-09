# Welcome message
# Enter the card
# Language selection - English, Hindi, Marathi
# Enter Pin
# Verify Pin
# Show Menu - Withdraw, Change Pin, Check balance
#   Withdraw - Saving, Current
#       Saving - Enter Amount
#           Processing Prompt and collect cash message
# Print Receipt option - Y/N
# Remove Card prompt
# Exit transaction

import time
from users import users

print("\nWELCOME TO THE GOTHAM CITY STATE BANK ATM NETWORK\n\n")
ins = input("Please press 'I' to insert your card for service >>> ")

if ins == "I":
    languages = ["English", "Hindi"]
    for lang_idx, language in enumerate(languages, start=1):
        print(f"{lang_idx}. {language}")
    lang_inp = input("Please select your preferred language >>> ")

    if lang_inp == "2":
        print("Sorry for the inconvenience, we couldn't set Hindi as your preferred language. English would be set by default.")

    attempt = 1

    while attempt <= 3:
        user_pin = int(input("Please enter your 4 digit ATM Pin >>> "))

        if user_pin in users:
            first_name = users[user_pin]["first_name"]
            last_name = users[user_pin]["last_name"]
            account_no = users[user_pin]["account_no"]
            balance = users[user_pin]["balance"]
            currency = users[user_pin]["currency"]
            print(
                f"Hello {first_name} {last_name[0]}.\nWhat would you like to do?")
            options = ["Withdraw", "Change Pin", "Check Balance"]

            for opt_idx, option in enumerate(options, start=1):
                print(f"{opt_idx}. {option}")

            opt_inp = int(input("Please select from the above options >>> "))

            while True:
                if opt_inp in [1, 2, 3]:
                    if opt_inp == 3:
                        print("Please wait...")
                        time.sleep(1.0)
                        print("We are fetching your account details...")
                        time.sleep(2.0)
                        print(f"Your account balance is {currency}{balance}.")
                    elif opt_inp == 1:
                        print("Please wait...")
                        time.sleep(1.0)
                        wdw_options = ["Savings Account", "Current Account"]

                        for wdw_idx, wdw_option in enumerate(wdw_options, start=1):
                            print(f"{wdw_idx}. {wdw_option}")

                        wdw_opt = int(input("Choose account >>> "))
                        if wdw_opt == 2:
                            print(
                                "You are not allowed to dispense from your Current Account.")
                            break
                        elif wdw_opt == 1:
                            wdw_inp = int(
                                input("Please enter the amount >>> $"))

                            if wdw_inp > balance:
                                print(
                                    "Cannot withdraw amount greater than account balance!")
                            else:
                                balance -= wdw_inp
                                print("Processing...")
                                time.sleep(2.0)
                                print("Please collect your cash!")
                                print(
                                    f"Your account balance is {currency}{balance}")

                    else:
                        print("Invalid input.")
                        break
                    else:
                        pass
                    break
                else:
                    print("Please select a valid option!")
            print(
                "Thanks for visiting GOTHAM CITY STATE BANK ATM NETWORK\nHave a good day!")
            break
        else:
            attempt += 1
            print(
                f"Invalid ATM Pin. You have {4 - attempt} attempts remaining.")

else:
    print("Card not inserted!\nThanks for visiting... Have a good day!")

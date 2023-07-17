import time

class Account:
    def __init__(self, name, number, place, balance):
        self.name = name
        self.number = number
        self.place = place
        self.balance = balance

    def display_info(self):
        print("Account Details:")
        print('Name:', self.name)
        print('Mobile numbers:', self.number)
        print('Place:', self.place)
        print('Your Current Balance:', self.balance)

    def balance_check(self):
        print("Your Account Current Balance:>", self.balance)

    def withdraw(self, withdraw_amount):
        if withdraw_amount <= self.balance:
            self.balance -= withdraw_amount
            print("Transaction Complete")
            print('Withdraw amount is', withdraw_amount)
            x = int(input('Press 1 for Check Current Balance\n'
                          'Press 2 for Exit'))
            if x == 1:
                print("Currently Account Balance is", self.balance)
        else:
            print('Insufficient balance. Check Your Balance')
            y = int(input('Press 1 for Check Current Balance\n'
                          'Press 2 for Exit'))
            if y == 1:
                print("Currently Account Balance is", self.balance)

    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        print("Transaction Complete")
        print("Deposited Amount is", deposit_amount)
        z = int(input('Press 1 for Check Current Balance\n'
                      'Press 2 for Exit'))
        if z == 1:
            print("Currently Account Balance is", self.balance)


bank = {}
print("Welcome to Tokyo Bank!")

while True:
    choice = int(input('Press 1 for Login\n'
                       'Press 2 for New Account Create.\n'
                       'Press 3 for Exit'))

    if choice == 1:
        username = input("Enter Your Username:")
        time.sleep(0.5)
        print('Please wait.\nLoading....')
        time.sleep(0.5)
        print('Loading.....')
        time.sleep(0.5)
        print('Loading................')
        time.sleep(1)

        if username in bank:
            account = bank[username]
            print('Welcome', username, '!')
            choice1 = int(input('Press 1 for Check Balance\n'
                                'Press 2 for Money Withdraw\n'
                                'Press 3 for Money Deposit\n'
                                'Press 4 for Account Details\n'
                                'Press 0 for Logout'))

            if choice1 == 1:
                account.balance_check()

            elif choice1 == 2:
                a = int(input('Press 1 for 1000\n'
                              'Press 2 for 2000\n'
                              'Press 3 for 3000\n'
                              'Press 4 for other amount'))

                if a == 1:
                    b = a
                elif a == 2:
                    b = a
                elif a == 3:
                    b = a
                elif a == 4:
                    other = int(input('Enter an amount'))
                    b = other
                else:
                    print("Invalid Input")

                account.withdraw(b)

            elif choice1 == 3:
                a = int(input('Press 1 for 1000\n'
                              'Press 2 for 2000\n'
                              'Press 3 for 3000\n'
                              'Press 4 for other amount'))

                if a == 1:
                    b = a
                elif a == 2:
                    b = a
                elif a == 3:
                    b = a
                elif a == 4:
                    other = int(input('Enter an amount'))
                    b = other
                else:
                    print("Invalid Input")

                account.deposit(b)

            elif choice1 == 4:
                account.display_info()

            elif choice1 == 5:
                print("Logged out successfully!!")
            else:
                print("Invalid Input")

        else:
            print("Account not found")
            print('===============================')

    elif choice == 2:
        name = input("Enter your full name:")

        while True:
            number = input("Enter your mobile number:")

            if number.isdigit() and len(number) == 10:
                break

            print("Enter a 10-digit mobile number")

        place = input('Enter your place and pincode:')
        balance = float(input('Add Account Opening amount'))

        account = Account(name, number, place, balance)
        bank[name] = account

        print('Your Account is created Successfully!!!')

    else:
        print("Invalid Option")

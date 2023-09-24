# Function to check each account balance
def checkAccountBalance():
    file = open("balance.txt")
    print("The balance in your chequing account is $" + file.readline().strip("\n") + ".")
    print("The balance in your savings account is $" + file.readline().strip("\n") + ".")
    file.close()

# Function to deposit money
def depositMoney(account, money):
    file = open("balance.txt")
    cheqAccount = float(file.readline().strip("\n"))
    savingsAccount = float(file.readline().strip("\n"))

    if account == "cheqAccount":
        cheqAccount += money
    else:
        savingsAccount += money
    file.close()

    file = open("balance.txt", "w")
    file.write(str("{:.2f}".format(cheqAccount) + "\n"))
    file.write(str("{:.2f}".format(savingsAccount) + "\n"))
    file.close()

# Function to withdraw money
def withdrawMoney(account, money):
    file = open("balance.txt")
    cheqAccount = float(file.readline().strip("\n"))
    savingsAccount = float(file.readline().strip("\n"))

    if account == "cheqAccount":
        if money <= cheqAccount:
            cheqAccount -= money
            print("\nFinished withdrawing money!\n")
        else:
            print("\nInsufficient balance! You cannot withdraw $" + str("{:.2f}".format(money)) + " out of your account.\n")

    else:
        if money <= savingsAccount:
            savingsAccount -= money
            print("\nFinished withdrawing money!\n")
        else:
            print("\nInsufficient balance! You cannot withdraw $" + str("{:.2f}".format(money)) + " out of your account.\n")
    file.close()

    file = open("balance.txt", "w")
    file.write(str("{:.2f}".format(cheqAccount) + "\n"))
    file.write(str("{:.2f}".format(savingsAccount) + "\n"))
    file.close()

# Function to transfer money
def transferMoney(accountTo, money):
    file = open("balance.txt")
    cheqAccount = float(file.readline().strip("\n"))
    savingsAccount = float(file.readline().strip("\n"))

    if accountTo == "cheqAccount":
        if money <= savingsAccount:
            cheqAccount += money
            savingsAccount -= money
            print("\nFinished transfering money!\n")
        else:
            print("Insufficient balance in Savings Account! Cannot perform transfer.")

    else:
        if money <= cheqAccount:
            savingsAccount += money
            cheqAccount -= money
            print("\nFinished transfering money!\n")
        else:
            print("Insufficient balance in Chequing Account! Cannot perform transfer.")
    file.close()

    file = open("balance.txt", "w")
    file.write(str("{:.2f}".format(cheqAccount) + "\n"))
    file.write(str("{:.2f}".format(savingsAccount) + "\n"))
    file.close()

# Function for first menu choice (account balance check)
def menuChoice1():
    print("\nChecking balance of accounts...\n")
    checkAccountBalance()
    print("\nFinished checking account balance!\n")

    continueBanking()

# Function for second menu choice (depositing money)
def menuChoice2(depositChoice):
    valid = False
    if depositChoice == "1":
        print("\nLoading chequing account...")

        while valid == False:
            try:
                depositMoneyChoice = float(input("\nHow much money would you like to deposit? $"))
                if depositMoneyChoice > 0:
                    valid = True
                else:
                    print("Please input a value greater than $0.00.")
            except:
                print("Invalid input. Please enter a number.")

        print("\nDepositing money...")
        depositMoney("cheqAccount", depositMoneyChoice)
        print("\nFinished depositing money!\n")

        continueBanking()

    elif depositChoice == "2":
        print("\nLoading savings account...")

        while valid == False:
            try:
                depositMoneyChoice = float(input("\nHow much money would you like to deposit? $"))
                if depositMoneyChoice > 0:
                    valid = True
                else:
                    print("Please input a value greater than $0.00.")
            except:
                print("Invalid input. Please enter a number.")

        print("\nDepositing money...")
        depositMoney("savingsAccount", depositMoneyChoice)
        print("\nFinished depositing money!\n")

        continueBanking()

    elif depositChoice == "0":
        print("\nReturning to main menu...\n")
        menu()

    else:
        print("\nInvalid input. Please enter the number\nthat correlates with your preferred action.")
        print("\nReturning to main menu...\n")
        menu()

# Function for third menu choice (withdrawing money)
def menuChoice3(withdrawChoice):
    valid = False
    if withdrawChoice == "1":
        print("\nLoading chequing account...")

        while valid == False:
            try:
                withdrawMoneyChoice = float(input("\nHow much money would you like to withdraw? $"))
                if withdrawMoneyChoice > 0:
                    valid = True
                else:
                    print("Please input a value greater than $0.00.")
            except:
                print("Invalid input. Please enter a number.")

        print("\nWithdrawing money...")
        withdrawMoney("cheqAccount", withdrawMoneyChoice)

        continueBanking()

    elif withdrawChoice == "2":
        print("\nLoading savings account...")

        while valid == False:
            try:
                withdrawMoneyChoice = float(input("\nHow much money would you like to withdraw? $"))
                if withdrawMoneyChoice > 0:
                    valid = True
                else:
                    print("Please input a value greater than $0.00.")
            except:
                print("Invalid input. Please enter a number.")

        print("\nWithdrawing money...")
        withdrawMoney("savingsAccount", withdrawMoneyChoice)

        continueBanking()

    elif withdrawChoice == "0":
        print("\nReturning to main menu...\n")
        menu()

    else:
        print("\nInvalid input. Please enter the number\nthat correlates with your preferred action.")
        print("\nReturning to main menu...\n")
        menu()

# Function for fourth menu choice (transfering money)
def menuChoice4(transferToChoice):
    valid = False
    if transferToChoice == "1":
        print("\nLoading accounts...")

        while valid == False:
            try:
                transferMoneyChoice = float(input("\nHow much money would you like to transfer from your savings account? $"))
                if transferMoneyChoice > 0:
                    valid = True
                else:
                    print("Please input a value greater than $0.00.")
            except:
                print("Invalid input. Please enter a number.")

        print("\nTransfering money...")
        transferMoney("cheqAccount", transferMoneyChoice)

        continueBanking()

    elif transferToChoice == "2":
        print("\nLoading accounts...")

        while valid == False:
            try:
                transferMoneyChoice = float(input("\nHow much money would you like to transfer from your chequing account? $"))
                if transferMoneyChoice > 0:
                    valid = True
                else:
                    print("Please input a value greater than $0.00.")
            except:
                print("Invalid input. Please enter a number.")

        print("\nTransfering money...")
        transferMoney("savingsAccount", transferMoneyChoice)

        continueBanking()

    else:
        print("\nReturning to main menu...\n")
        menu()

# Function to ask user if they would like to continue banking
def continueBanking():
    cont = input("Would you like to continue with online banking (Y/N)? ").upper()

    while cont != "Y" and cont != "N":
        cont = input("Please enter either \"Y\" for yes and \"N\" for no: ").upper()

    if cont == "Y":
        print("\nOkay! Continuing online banking...\n")
        menu()
    else:
        print("\nLogging out...\n")
        print("Logged out successfully.")

# Menu function
def menu():
    print("---------ONLINE BANKING---------")
    print("\nWelcome to your account. Please\npick an option from this menu.\n")
    print(" [1] -- Check account balances")
    print(" [2] -- Deposit money")
    print(" [3] -- Withdraw money")
    print(" [4] -- Transfer money")
    print(" [0] -- Log out")

    menuChoice = input("\nWhat would you like to do today? ")
    menuChoice = menuChoice.strip() # Just in case the user put spaces in the input

    if menuChoice == "1": # For account balance check
        menuChoice1()

    elif menuChoice == "2": # For depositing money
        print("\nBelow are your available accounts.\n")
        print(" [1] -- Chequing Account")
        print(" [2] -- Savings Account")
        print(" [0] -- Return to main menu")

        depositChoice = input("\nWhich account would you like to deposit money into? ")
        depositChoice = depositChoice.strip()

        menuChoice2(depositChoice)

    elif menuChoice == "3": # For withdrawing money
        print("\nBelow are your available accounts.\n")
        print(" [1] -- Chequing Account")
        print(" [2] -- Savings Account")
        print(" [0] -- Return to main menu")

        withdrawChoice = input("\nWhich account would you like to withdraw money from? ")
        withdrawChoice = withdrawChoice.strip()

        menuChoice3(withdrawChoice)

    elif menuChoice == "4": # For transfering money
        transferFromChoice = ""
        transferToChoice = ""
        print("\nBelow are your available accounts.\n")
        print(" [1] -- Chequing Account")
        print(" [2] -- Savings Account")
        print(" [0] -- Return to main menu")

        while transferFromChoice == transferToChoice:
            transferFromChoice = input("\nWhich account would you like to transfer money from? ")
            transferFromChoice = transferFromChoice.strip()

            if transferFromChoice == "0":
                print("\nReturning to main menu...\n")
                menu()

            elif transferFromChoice != "1" and transferFromChoice != "2":
                transferToChoice = transferFromChoice # So the loop will continue
                print("\nInvalid input. Please enter the number\nthat correlates with your preferred action.")
                
            else:
                transferToChoice = input("Which account would you like to transfer money to? ")
                transferToChoice = transferToChoice.strip()

                if transferFromChoice == transferToChoice:
                    print("\nYou can only transfer money from different accounts.")

                elif transferToChoice != "1" and transferToChoice != "2" and transferToChoice != "0":
                    transferFromChoice = transferToChoice # So the loop will continue
                    print("\nInvalid input. Please enter the number\nthat correlates with your preferred action.")
                    
                else:
                    menuChoice4(transferToChoice)

    elif menuChoice == "0": # For logging out
        print("\nLogging out...\n")
        print("Logged out successfully.")

    else: # For an invalid input
        print("\nInvalid input. Please enter the number\nthat correlates with your preferred action.")
        print("\nReturning to main menu...\n")
        menu()

menu()

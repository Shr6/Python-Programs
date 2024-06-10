#Python Banking System

def show_balance(balance):
    # Display the current balance
    print("*******************")
    print(f"Your balance is {balance:.2f} Rs")
    print("*******************")

def deposit():
    # Prompt the user to enter an amount to deposit
    print("*******************")
    amount = float(input("Enter an amount to be deposited: "))
    print("*******************")
    
    # Check if the deposit amount is valid
    if amount < 0:
        print("*******************")
        print("It is not a valid amount")
        print("*******************")
        return 0
    else:
        return amount

def withdraw(balance):
    # Prompt the user to enter an amount to withdraw
    print("*******************")
    amount = float(input("Enter amount to be withdrawn: "))
    print("*******************")
    
    # Check if the withdrawal amount is greater than the balance or negative
    if amount > balance:
        print("*******************")
        print("Insufficient funds:")
        print("*******************")
        return 0
    elif amount < 0:
        print("*******************")
        print("Amount must be greater than 0")
        print("*******************")
        return 0
    else:
        return amount

def main():
    balance = 0  # Initial balance
    is_running = True  # Flag to control the program loop

    while is_running:
        # Display the main menu
        print("*******************")
        print("  Banking Program  ")
        print("*******************")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("*******************")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            # Show the current balance
            show_balance(balance)
        elif choice == '2':
            # Deposit an amount and update the balance
            balance += deposit()
        elif choice == '3':
            # Withdraw an amount and update the balance
            balance -= withdraw(balance)
        elif choice == '4':
            # Exit the program
            is_running = False
        else:
            # Handle invalid menu choices
            print("*******************")
            print("That is not a valid entry")
            print("*******************")
    
    # Goodbye message when the program exits
    print("*******************")
    print("Thank you, have a nice day!")
    print("*******************")

# If this script is executed, run the main function
if __name__ == '__main__':
    main()

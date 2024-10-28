
class BankAccount:
    def __init__(self, account_number):
        self.account_number = account_number  # Initialize the account number
        self.balance = 0  # Set the initial balance to 0

    def deposit(self, amount):
        if amount > 0:  # Check if the amount is positive
            self.balance += amount  # Add the amount to the balance
            print(f"Deposited ${amount}. New balance: ${self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:  # Check if the amount is positive and less than or equal to the balance
            self.balance -= amount  # Subtract the amount from the balance
            print(f"Withdrew ${amount}. New balance: ${self.balance}.")
        elif amount > self.balance:
            print("Insufficient funds for this withdrawal.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        return f"Current balance: ${self.balance}"  # Return the current balance


def main():
    account_number = input("Enter your account number: ")  # Prompt user for account number
    account = BankAccount(account_number)  # Create an instance of BankAccount

    while True:  # Start an indefinite loop
        print("\nOptions: (a) Deposit, (b) Withdraw, (c) Check Balance, (d) Exit")
        choice = input("Choose an option: ").strip().lower()  # Prompt user for an action

        if choice == 'a':
            amount = float(input("Enter amount to deposit: "))  # Prompt for deposit amount
            account.deposit(amount)  # Call the deposit method
        elif choice == 'b':
            amount = float(input("Enter amount to withdraw: "))  # Prompt for withdrawal amount
            account.withdraw(amount)  # Call the withdraw method
        elif choice == 'c':
            print(account.check_balance())  # Display the current balance
        elif choice == 'd':
            print("Thank you for using the bank account system. Goodbye!")  # Exit message
            break  # Break the loop to exit the program
        else:
            print("Invalid option. Please choose again.")  # Handle invalid options


if __name__ == "__main__":
    main()  # Run the main function



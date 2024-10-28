# McCullerFP7-ds3850


### Code Explanation: FP7GuessingGame.py

1. **Import the `random` module**:
   - This allows us to use functions to randomize the order of the questions.

2. **Define the `quiz_bowl` function**:
   - This function contains all the logic for the quiz game.

3. **Create a dictionary called `questions_answers`**:
   - The keys are the questions, and the values are the corresponding correct answers.

4. **Randomize the questions**:
   - Convert the dictionary keys (questions) into a list.
   - Use `random.shuffle()` to shuffle the list in place, randomizing the order of the questions.

5. **Loop through the randomized questions**:
   - For each question in the shuffled list:
     - Print the question to the console.
     - Use `input()` to prompt the user for their answer, stripping any extra spaces.

6. **Check the user's answer**:
   - Compare the user's input (converted to lowercase for case-insensitivity) with the correct answer (also converted to lowercase).
   - If the answer is correct, print "Correct!".
   - If the answer is incorrect, print "Wrong!" followed by the correct answer.

7. **Print a completion message**:
   - After all questions have been asked, print a thank-you message.

8. **Run the `quiz_bowl` function**:
   - The program starts executing from this point when run directly.


### Explanation of the Code: FP7ColorFulText

1. **Define Color Functions**:
   - Each function (`redText`, `blueText`, `greenText`, `yellowText`, `brownText`) takes a string as input and returns it wrapped in ANSI escape codes that change the text color when printed in a terminal that supports ANSI codes.

2. **Main Function**:
   - Calls each color function to display predefined messages in their respective colors.
   - Prompts the user to choose a color and input a custom string.
   - Based on the user's color choice, it calls the corresponding function to display the user's text in the chosen color.

3. **Input Validation**:
   - If the user enters an invalid color choice, the program informs them of the error.

### Explanation of the Code: FP7BankClass

1. **Class Definition**:
   - `class BankAccount:`: Defines a class named `BankAccount`.
   - `def __init__(self, account_number):`: This is the constructor method that initializes the account with an account number and sets the initial balance to 0.
   - `self.account_number = account_number`: Assigns the provided account number to the instance attribute.
   - `self.balance = 0`: Initializes the balance attribute to 0.

2. **Deposit Method**:
   - `def deposit(self, amount):`: Method to handle deposits.
   - `if amount > 0:`: Checks if the deposit amount is positive.
   - `self.balance += amount`: Adds the deposit amount to the balance.
   - `print(...)`: Prints the updated balance.

3. **Withdraw Method**:
   - `def withdraw(self, amount):`: Method to handle withdrawals.
   - `if 0 < amount <= self.balance:`: Checks if the withdrawal amount is positive and does not exceed the current balance.
   - `self.balance -= amount`: Subtracts the withdrawal amount from the balance.
   - `elif amount > self.balance:`: Checks for insufficient funds and informs the user.
   - `else:`: Informs the user if the withdrawal amount is non-positive.

4. **Check Balance Method**:
   - `def check_balance(self):`: Method to return the current balance.
   - `return f"Current balance: ${self.balance}"`: Returns the current balance as a formatted string.

5. **Main Function**:
   - `def main():`: Defines the main function to execute the program.
   - `account_number = input(...)`: Prompts the user to enter their account number.
   - `account = BankAccount(account_number)`: Creates an instance of `BankAccount` using the provided account number.
   - `while True:`: Starts an indefinite loop to allow repeated actions.
   - `print(...)`: Displays the options for the user.
   - `choice = input(...):`: Prompts the user to choose an action.
   - Based on the user’s choice, calls the appropriate method (deposit, withdraw, check balance) or exits the loop if the user chooses to exit.
   - Handles invalid options by prompting the user again.

6. **Execution**:
   - `if __name__ == "__main__":`: Ensures that the `main` function runs only if the script is executed directly.

This program provides a simple bank account management system that can be expanded with more features as needed.
# McCullerFP7-ds3850

### Explanation of the Code:FP7madlib.py

1. **Define the `main` Function**:
   - `def main():`: This line defines the main function where the program logic will reside.

2. **Prompt User for Inputs**:
   - Each `input()` function prompts the user to enter specific types of words:
     - `adjective = input("Enter an adjective: ")`: Asks for an adjective.
     - `large_objects_plural = input("Enter a plural large object: ")`: Asks for a plural noun referring to large objects.
     - `body_part = input("Enter a body part: ")`: Asks for a body part.
     - `restaurant = input("Enter a restaurant name: ")`: Asks for a name of a restaurant.
     - `first_food = input("Enter a type of food: ")`: Asks for a type of food.
     - `second_food = input("Enter another type of food: ")`: Asks for another type of food.
     - `large_object_singular = input("Enter a large object (singular): ")`: Asks for a singular large object.

3. **Create the Filled-in Story**:
   - The `story` variable uses an f-string to format the collected inputs into a complete story:
     - Each placeholder in the string (like `{adjective}`) is replaced by the user’s input.
     - The multiline f-string allows for better readability.

4. **Print the Completed Story**:
   - `print("\nHere's your story:")`: Prints a message indicating the output will follow.
   - `print(story)`: Displays the final story that includes all the user inputs.

5. **Execution Block**:
   - `if __name__ == "__main__":`: This checks if the script is being run directly (not imported).
   - `main()`: Calls the main function to execute the program.


### Explanation of the Code:FP7powerball.py

1. **Import Statements**:
   - `import random`: This imports the `random` module, allowing us to generate random numbers.
   - `import time`: This imports the `time` module, which provides the `sleep` function to pause execution.

2. **Define the `main` Function**:
   - `def main():`: Defines the main function where the program logic will be implemented.

3. **Greeting the Player**:
   - `print("Welcome to the Powerball drawing!")`: Displays a welcome message.
   - `time.sleep(1)`: Pauses the program for 1 second to create a delay before the next message.
   - `print("The Powerball numbers are about to be drawn...")`: Informs the player that the drawing is about to occur.
   - Another `time.sleep(1)` to maintain the delay.

4. **Generating Powerball Numbers**:
   - `powerball_numbers = random.sample(range(1, 70), 5)`: Generates a list of 5 unique random numbers between 1 and 69.
   - `for num in powerball_numbers:`: Loops through each generated number.

5. **Printing Numbers**:
   - `print(f"Your next number is: {num}")`: Displays the current number being drawn.
   - `time.sleep(1)`: Waits for 1 second before proceeding to the next number.

6. **Announcing the Powerball**:
   - `print("And now it's time for the Powerball...")`: Indicates that the Powerball number will be drawn next.
   - Another `time.sleep(1)` for a pause.

7. **Generating the Powerball Number**:
   - `powerball = random.randint(1, 26)`: Generates a random number for the Powerball (between 1 and 26).
   - `print(f"The Powerball number is: {powerball}")`: Displays the Powerball number.
   - `time.sleep(1)` to wait before moving on.

8. **Displaying All Numbers**:
   - `all_numbers = ', '.join(map(str, powerball_numbers)) + f", and the Powerball number is: {powerball}"`: Combines the list of Powerball numbers and the Powerball into a single formatted string.
   - `print("\nAll your numbers are:", all_numbers)`: Displays all the numbers in one line.
   - Another `time.sleep(1)` for the final pause.

9. **Thanking the Player**:
   - `print("Thank you for playing! Goodbye!")`: Displays a farewell message.

10. **Execution Block**:
   - `if __name__ == "__main__":`: This checks if the script is being run directly.
   - `main()`: Calls the main function to execute the program.

This program simulates a Powerball drawing with clear user feedback and appropriate pauses, making it interactive and engaging. You can run it in a Python environment to see how it works!


### Explanation of the Code: FP7GuessingGame.py

1. **Import the `random` module**: 
   - Allows for the generation of random numbers.

2. **Define the `play_guessing_game` function**:
   - This function contains the logic for the guessing game.
   - A random number between 1 and 10 is generated.
   - The user is prompted to guess the number repeatedly until they guess correctly.
   - After each guess, feedback is provided to indicate if the guess is too low or too high.

3. **Define the `main` function**:
   - This function controls the game flow.
   - It prompts the user to decide if they want to play.
   - If the user responds with anything other than "yes," a message is displayed, and the loop ends.
   - If they choose to play, the `play_guessing_game` function is called.
   - After the game concludes, the user is asked if they want to play again.

4. **Input validation**:
   - The program checks if the input is a digit and within the valid range (1-10).
   - If not, it prompts the user to enter a valid number.

5. **Game loop**:
   - The game allows the user to play multiple rounds without asking for the initial question again after the first play.

6. **Run the program**:
   - The last line ensures the `main` function is executed when the script is run directly.


### Code Explanation: FP7QuizBowl.py

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
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


### Explanation of the Code: FP7ColorFullText

1. **Define Color Functions**:
   - Each function (`redText`, `blueText`, `greenText`, `yellowText`, `brownText`) takes a string as input and returns it wrapped in ANSI escape codes that change the text color when printed in a terminal that supports ANSI codes.

2. **Main Function**:
   - Calls each color function to display predefined messages in their respective colors.
   - Prompts the user to choose a color and input a custom string.
   - Based on the user's color choice, it calls the corresponding function to display the user's text in the chosen color.

3. **Input Validation**:
   - If the user enters an invalid color choice, the program informs them of the error.


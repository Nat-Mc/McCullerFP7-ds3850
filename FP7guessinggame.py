import random

def guessing_game():
    while True:
        # Start the game
        play = input("Do you want to play a guessing game? (yes/no): ").strip().lower()
        
        if play != 'yes':
            print("Maybe next time!")
            break

        # Generate a random number between 1 and 10
        number_to_guess = random.randint(1, 10)
        guess = None
        
        # Game loop for guessing the number
        while guess != number_to_guess:
            guess = input("Guess a number between 1 and 10: ")
            
            # Validate input
            if not guess.isdigit() or not (1 <= int(guess) <= 10):
                print("Please enter a valid number between 1 and 10.")
                continue
            
            guess = int(guess)
            
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
        
        # User guessed correctly
        print(f"Congratulations! You guessed the correct number: {number_to_guess}")
        
        # Ask if the user wants to play again without repeating the initial question
        again = input("Do you want to play again? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Thank you for playing! Goodbye!")
            break

if __name__ == "__main__":
    guessing_game()

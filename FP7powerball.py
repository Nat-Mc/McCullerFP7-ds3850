import random
import time

def main():
    # Greet the player
    print("Welcome to the Powerball drawing!")
    time.sleep(1)
    print("The Powerball numbers are about to be drawn...")
    time.sleep(1)

    # Generate five unique Powerball numbers from 1 to 69
    powerball_numbers = []
    for _ in range(5):
        num = random.randint(1, 69)
        while num in powerball_numbers:
            num = random.randint(1, 69)
        powerball_numbers.append(num)
        print(f"Your next number is: {num}")
        time.sleep(1)

    # Indicate that the Powerball is next
    print("And now it's time for the Powerball...")
    time.sleep(1)

    # Generate the Powerball number from 1 to 26
    powerball = random.randint(1, 26)
    print(f"The Powerball number is: {powerball}")
    time.sleep(1)

    # Reprint all the previous numbers in a single line
    all_numbers = ', '.join(map(str, powerball_numbers)) + f", and the Powerball number is: {powerball}"
    print("\nAll your numbers are:", all_numbers)
    time.sleep(1)

    # Thank the player and wish them goodbye
    print("Thank you for playing! Goodbye!")

if __name__ == "__main__":
    main()

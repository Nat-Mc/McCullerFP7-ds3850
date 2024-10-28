def redText(text):
    return f"\033[91m{text}\033[0m"

def blueText(text):
    return f"\033[94m{text}\033[0m"

def greenText(text):
    return f"\033[92m{text}\033[0m"

def yellowText(text):
    return f"\033[93m{text}\033[0m"

def brownText(text):
    return f"\033[95m{text}\033[0m"  # Magenta as a close approximation for brown

def main():
    # Call each function and print the colored text
    print(redText("This is red text"))
    print(blueText("This is blue text"))
    print(greenText("This is green text"))
    print(yellowText("This is yellow text"))
    print(brownText("This is brown text"))

    # User input for custom text color
    color_choice = input("Choose a color (red, blue, green, yellow, brown): ").strip().lower()
    user_text = input("Enter the text you want to display: ")

    # Display the text in the chosen color
    if color_choice == "red":
        print(redText(user_text))
    elif color_choice == "blue":
        print(blueText(user_text))
    elif color_choice == "green":
        print(greenText(user_text))
    elif color_choice == "yellow":
        print(yellowText(user_text))
    elif color_choice == "brown":
        print(brownText(user_text))
    else:
        print("Invalid color choice. Please choose from red, blue, green, yellow, or brown.")

if __name__ == "__main__":
    main()

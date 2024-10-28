import random

def quiz_bowl():
    # Dictionary of questions and answers
    questions_answers = {
        "What is the capital of France?": "Paris",
        "What is 2 + 2?": "4",
        "What is the largest ocean on Earth?": "Pacific",
        "Who wrote 'Romeo and Juliet'?": "Shakespeare",
        "What is the smallest prime number?": "2"
    }
    
    # Randomize the questions
    questions = list(questions_answers.keys())
    random.shuffle(questions)

    # Loop through the questions
    for question in questions:
        # Display the question
        print(question)
        # Prompt the user for their answer
        user_answer = input("Your answer: ").strip()

        # Check if the user's answer is correct
        if user_answer.lower() == questions_answers[question].lower():
            print("Correct!")
        else:
            print(f"Wrong! The correct answer is: {questions_answers[question]}")
    
    print("Quiz complete! Thank you for playing!")

if __name__ == "__main__":
    quiz_bowl()

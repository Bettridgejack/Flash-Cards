import random
# This imports the random module to our code so we can randomly select flashcards from the flashcard dictionary we are going to create

flashcard = {
    "Question 1": "Answer 1",
    "Question 2": "Answer 2",
    "Question 3": "Answer 3", 
    "Question 4": "Answer 4",
}
# This is the flashcard dictionary. it stores data in a key-value format, so in this case we have the key (Question) and the value (answer)

def show_flashcard():
    question = random.choice(list(flashcard.keys()))
    # This is telling us that the question is going to be a random choice selected from the list of options in the flashcard dictionary.
    # We have added the .key because we specifically want the question which is the key part of the flashcard dictionary.
    print(f"Your question is: {question}")
    # This now prints the question. we use an f in the function so we can call on the question value we just defined and print it.
    answer = input("Your Answer: ").lower()
    # This now tells the user to input their answer and then hopefully converts it into lower case to avoid any issues. 

    if answer.strip().lower() == flashcard[question].lower():
    # .strip removes the spaces and .lower makes it all lower case 
    #  so it is saying that if the answer is equal to the flashcard key value defined in the dictionary, then we print correct.
        print("Correct!")
    else:
        print(f"Incorrect. the answer was {flashcard[question]}")
        # This says that if the answer is incorrect, then we print the correct answer.

def add_flashcard():
    question = input("What question would you like to add?: ")
    # This gets the user to type the question they want to add to the dictionary.
    answer = input("What is the answer?: ")
     # This gets them to type the answer to that question.
    flashcard[question] = answer
    # This tells the flashcard dictionary that the key (question) is equal to the value (Answer) and to add it to the dictionary.
    print("Flashcard added succesfully")

def main():
    while True:
        print("\nWhich option would you like to pick?: ")
        print("1: Show a Flashcard.")
        print("2: Add a Flashcard")
        print("3: Exit")
    # this is printing out all of the options which we will route afterwards. first of all we need to assign a value to the choice. 
        choice = input("Please select a choice: ")

        if choice == "1":
            show_flashcard()
        # This tells us that if the user selects option 1, then we run the show_flashcard function that we programmed above.
        elif choice == "2":
            add_flashcard()
        # This tells us that if the user slects option 2, then we need to run the aff flashcard option that we defined above.
        elif choice == "3":
            print("Goodbye")
            break
        # This bit just means if they press exit, then we stop running the program and it prints goodbye to the user. it breaks the loop.
        else:
            print("Please choose an option from the list: ")
        # This is just a graceful way to handle an invalid input from the user.

main()



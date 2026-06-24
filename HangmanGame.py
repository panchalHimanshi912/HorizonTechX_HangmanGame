import random

# Word list
words = ["python", "apple", "laptop", "coding", "india"]

# Random word choose
word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("Welcome to Hangman Game!")

while wrong_guesses < max_wrong:

    # Display word
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Win condition
    if "_" not in display_word:
        print(" Congratulations! You guessed the word:", word)
        break

    # User input
    guess = input("Enter a letter: ").lower()

    # Check letter
    if guess in word:
        print(" Correct Guess!")
        guessed_letters.append(guess)
    else:
        print(" Wrong Guess!")
        wrong_guesses += 1
        print("Remaining chances:", max_wrong - wrong_guesses)

# Lose condition
if wrong_guesses == max_wrong:
    print("\n Game Over!!!!!")
    print("The word was:", word)
import random

# List of 5 predefined words
words = ["apple", "tiger", "chair", "table", "robot"]

# Choose a random word
word = random.choice(words)

guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6

print("=== HANGMAN GAME ===")

while incorrect_guesses < max_incorrect:
    display = ""

    # Display the word
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    # Check if the player has guessed the word
    if "_" not in display:
        print("🎉 Congratulations! You guessed the word:", word)
        break

    print("Incorrect guesses left:", max_incorrect - incorrect_guesses)

    # Get user input
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check the guess
    if guess in word:
        print("Correct!")
    else:
        incorrect_guesses += 1
        print("Wrong!")

# Game over
if incorrect_guesses == max_incorrect:
    print("\nGame Over!")
    print("The correct word was:", word)

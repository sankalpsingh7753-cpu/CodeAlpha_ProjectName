# Hangman Game
import random  

# 1. List of 5 predefined words (all computer/technology related)
words = ["python", "computer", "program", "keyboard", "internet"]

# 2. The computer randomly chooses one word from the list
secret_word = random.choice(words)

# 3. Variables to keep track of the game
guessed_letters = []     # every letter the player has guessed so far
incorrect_guesses = 0    # number of wrong guesses
max_incorrect = 6        # the player loses after 6 wrong guesses
word_guessed = False     # becomes True when the whole word is revealed

# 4. Welcome message
print("========================")
print("      HANGMAN GAME")
print("========================")
print()
print("Guess the word one letter at a time.")
print()

# 5. Game loop: keeps running until the word is guessed OR 6 wrong guesses
while incorrect_guesses < max_incorrect and not word_guessed:

    # Build the word to show: real letter if guessed, otherwise an underscore
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word = display_word + letter + " "
        else:
            display_word = display_word + "_ "

    # Build the text that shows the guessed letters
    if len(guessed_letters) == 0:
        guessed_text = "-"
    else:
        guessed_text = ", ".join(guessed_letters)

    # Show the current status of the game
    print("Word: " + display_word)
    print("Incorrect guesses: " + str(incorrect_guesses) + "/" + str(max_incorrect))
    print("Guessed letters: " + guessed_text)
    print()

    # Ask for a guess; lower() makes uppercase and lowercase the same
    guess = input("Enter a letter: ").lower().strip()
    print()

    # Check the guess
    if len(guess) != 1 or not guess.isalpha():
        # Not exactly one letter (e.g. empty, a number, or many characters)
        print("Invalid input! Please enter only one letter (a-z).")
    elif guess in guessed_letters:
        # The player already tried this letter - not counted as a wrong guess
        print("You already guessed that letter. Try another one.")
    elif guess in secret_word:
        # Correct guess: remember it so it gets revealed
        guessed_letters.append(guess)
        print("Correct guess!")
    else:
        # Wrong guess: remember it and add 1 to the wrong-guess counter
        guessed_letters.append(guess)
        incorrect_guesses = incorrect_guesses + 1
        remaining = max_incorrect - incorrect_guesses
        print("Wrong guess!")
        print("Remaining attempts: " + str(remaining))

    print()

    # Check if every letter of the secret word has been guessed
    word_guessed = True
    for letter in secret_word:
        if letter not in guessed_letters:
            word_guessed = False

# 6. The loop has ended - show the result
if word_guessed:
    print("Word: " + " ".join(secret_word))
    print()
    print("Congratulations! You guessed the word: " + secret_word)
    print("Incorrect guesses made: " + str(incorrect_guesses))
else:
    print("Game over! You used all " + str(max_incorrect) + " incorrect guesses.")
    print("The correct word was: " + secret_word)

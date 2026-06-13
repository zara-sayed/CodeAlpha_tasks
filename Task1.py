import random

words = ["python", "fishtank", "college", "network", "student"]

print("===== HANGMAN GAME =====")

while True:   # Outer loop for multiple games

    word = random.choice(words)

    guessed_letters = []
    wrong_guesses = 0
    max_wrong = 6

    print("\nGuess the word one letter at a time.")
    print("You have 6 incorrect guesses.\n")

    while wrong_guesses < max_wrong:

        display_word = ""

        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("Word:", display_word)

        if "_" not in display_word:
            print("\n🎉 Congratulations! You guessed the word:", word)
            break

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabet.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct!\n")
        else:
            wrong_guesses += 1
            print("Wrong guess!")
            print("Remaining chances:", max_wrong - wrong_guesses, "\n")

    if wrong_guesses == max_wrong:
        print("\n❌ Game Over!")
        print("The correct word was:", word)

    # Ask user if they want another word
    play_again = input("\nDo you want to play again? (y/n): ").lower()

    if play_again != "y":
        print("\nThanks for playing! 👋")
        break

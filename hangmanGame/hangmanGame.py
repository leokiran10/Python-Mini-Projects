import random
import hangman_art
import hangmanword

#Randomly choose a word
selected_word = random.choice(hangmanword.word_list)

# List of length of selected word
display = ["_"] * len(selected_word)

print(hangman_art.logo)

lives = 7
stage = 0

end_of_game = False
while  not end_of_game:
    # Guess a letter
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You have already guessed {guess} letter.")

    i = 0
    for letter in selected_word:
        i = i+1
        if letter == guess:
            display[i-1] = letter

    if guess not in selected_word:
        print(f"You guessed {guess}, that's not in word. You lose a life.")
        lives = lives - 1
        print(f"Remaning lives: {lives}")
        stage = stage +1
        if lives == 0:
            end_of_game = True
            print("Sorry, You loose!")


    print(" ".join(display) + "\n")
    print(hangman_art.hangman_stages[stage-1])

    if "_" not in display:
        end_of_game = True
        print("Congrualtions, You win!")

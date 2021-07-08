#Step 5

import random
import hangman_art
import hangman_words
# from replit import clear

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]
stages = hangman_art.stages
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.

#Testing code
print(hangman_art.logo)

# print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
guessed = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    print(f"you already guessed {guessed}")
    guess = input("Guess a letter: ").lower()
    guessed += guess
    guessed.sort()
    
    if guess in display:
        print(f"you already guessed '{guess}' dummy. try again.")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        
        print(f"nope! '{guess}' isn't right")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The word you were looking for was {chosen_word}")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # Print gallows
    print(stages[lives])

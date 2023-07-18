import random
import hangman_words
import hangman_art

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

hangman_logo = hangman_art.logo
print(hangman_logo)
print(f"\nWelcome to Hangman. \nIt is a {word_length} letter word.\n")


#Testing code: print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
print(display)

while not end_of_game:
    guess = input("\nGuess a letter: ").lower()
    
    if guess in display:
          print("You've already guessed this letter: ", guess)

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
   
    #Check if user is wrong.
    if guess not in chosen_word:
          lives -= 1
          print(f"{guess} ,this letter is not in the word. You lose a life.")
          if lives == 0:
            end_of_game = True
            print("Game Over")
            print(f"The word to be guessed was: {chosen_word}.")
    
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    stages = hangman_art.stages

    print(stages[lives])
#Imports
import random
import sys
from termcolor import colored
from list import word_list

#for loop to iterate words of words_list and return teh word lowercase.
for i in range(len(word_list)):
    word_list[i] = word_list[i].lower()


# function that chooses random word from the words list.
words = word_list
word = random.choice(words)
print(word)

# Start game instructions press "" to start game.
welcome = input("Welcome to Python Wordl game! \n \n Instructions: \n \n You get 6 tries to guess the correct 5 letter word. \n If a letter turn up green it means it is in the right place \n if a letter turn upp yellow it means that is in the word but in another place. \n If your letter turn up red it is the wrong letter! \n \n GLHF! \n \n Press 'Enter' to continue! \n \n")

#input to be displayed through out the game
def game_display():
    print('please guess a 5 letter word and press "Enter"!\n')
    

game_display()

replay_game = ""
while replay_game != "q":
    for tries in range(1, 7):
        guess = input().lower()

        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')

        if len(guess) > 5:
            print(colored("Your word is too long, only 5 letters please!\n", 'red'), end="")
        elif len(guess) < 5:
            print(colored("Your word is too short, 5 letters please!\n", 'red'), end="")
        if not guess.isalpha():
            print(colored("Only letters are allowed!", 'red'), end="")

        for i in range(len(guess), len(guess)):
            if guess[i] == word[i]:
                print(colored(guess[i], 'green'), end="")
            elif guess[i] in word:
                print(colored(guess[i], 'yellow'), end="")
            else:
                print(guess[i], end="")
        print()

        if guess == word:
            print(colored(f"Awsome! You gussed the the right word in {tries} tries.", 'green'))
            break
        elif tries == 6: 
            print(colored("GAME OVER no more guesses!\n", 'red'), end="")
            break
    replay_game = print("Press 'Enter' to replay or to Quit game press 'q'")
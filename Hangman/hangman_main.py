# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 12:49:41 2021

@author: Will Lacey
"""
import hangman_game # Importing module for hangman game.
from hangman_board import Board # Importing module for hangman board.
from sys import exit

# Validating user's input for options from welcome screen
def validate_input(message):
    valid = False
    while not valid:
        try:
            user_input = int(input(message))
            if user_input in range(1,4): # Checks if user enters an option between 1 and 3.
                valid = True
            else:
                print('\nPlease enter one of the given options.')
        except:
            print('\nPlease enter a valid integer.')
    return user_input

# Will direct the program to the proper set code to execute based on user's decision.
def get_options(user_choice):
    if user_choice == 1:
        game_on()
    elif user_choice == 2:
        get_rules()
    else:
      exit_game()  

# Will start the hangman game by calling the imported module starting at main().
def game_on():
    hangman_game.main()

# Prints out the docstring that explains the rules.
def get_rules():
    """
    CPU will think of a word or phrase; the player will try to guess what it is 
    one letter at a time. The CPU will draw a number of asterisks equivalent to 
    the number of letters in the word/phrase. If the player suggests a letter 
    that occurs in the word, the CPU fills in the blanks with that letter in the 
    right places. If the word does not contain the suggested letter, the CPU 
    draws one element of hangman on the gallows. As the game progresses, a 
    segment of the victim is added for every suggested letter not in the word. 
    The number of incorrect guesses before the game ends is six as it will 
    complete the victim in a noose.
    """
    print(get_rules.__doc__)
    main() # Returns to main()/welcome screen.

# Will exit the game.
def exit_game():
    print('\nGame Over')
    exit() 
    
def main():
    # Welcome screen is below with initial options.
    print('Welcome to Hangman!')
    print(Board.HANGMAN.value[-1])
    print('\nEnter 1 to play Hangman.')
    print('Enter 2 for rules.')
    print('Enter 3 to exit the game.')
    
    # User inputs an option. 
    message = 'Enter 1, 2, or 3: '
    user_choice = validate_input(message)
    
    # Will direct the program to the proper set code to execute based on user's decision.
    get_options(user_choice)
        
if __name__ == '__main__':
    main()
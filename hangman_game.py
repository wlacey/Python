# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 15:01:52 2021

@author: Will Lacey
"""
from hangman_board import Board # Importing module for hangman board.
from random import choice
from re import finditer
from sys import exit

# Validates the number of rounds the user inputted. 
def validate_input(message):
    valid = False
    while not valid:
        try:
            user_input = int(input(message))
            if user_input > 0:
                valid = True
            else:
                print('\nPlease enter a proper amount of rounds.')
        except:
            print('\nPlease enter a positive integer.')
    return user_input

# Will grab a random phrase from hangman_words.txt. 
def get_phrase():
    # lines returns a list of all the phrases in the text file.
    lines = [line.strip() for line in open('hangman_words.txt')]
    return choice(lines) # Returns a random item from the lines list

# Will encrypt the random phrase. Also, else statement not needed just there to explicitly state.
def get_encrypt_phrase(phrase):
    for i in phrase:
        if i.isalpha():
            phrase = phrase.replace(i, '*')
        else:
            pass
    return phrase

# Validates whether or not the player inputted a letter or not.
def validate_guess(user_guess):
    valid = False
    while not valid:
        try:
            user_input = input(user_guess)
            if user_input.isalpha():
                valid = True
            else:
                print('\nPlease enter a letter as a guess.')
        except:
            pass   
    return user_input.lower()

# Check if the player wins or loses the match.
def winner_check(num_guess, phrase, encrypt_phrase, score):
    win = False
    if num_guess == 0:
        print(f'\nYou ran out of guesses. The phrase is "{phrase}". You lose.')
    elif phrase == encrypt_phrase:
        print(f'\nYes the phrase was "{phrase}".')
        print('You Win!')
        win = True
        score += 1
    return win

# The Hagman game will start here.
def game_on(phrase, encrypt_phrase):
    i = 0 # Iterator for the single, corresponding Hangman round.
    num_guess = 7 # Number of guesses the player has.
    
    while i < len(Board.HANGMAN.value):
        # Will print the hangman board from the imported module.
        print(Board.HANGMAN.value[i]) 
        # Will print the encrypted phrase and will have the correct letters there if guessd right.
        print(encrypt_phrase) 
        
        # Player will enter a letter and it will be validated.
        user_guess = 'Enter a letter: '
        letter = validate_guess(user_guess)
        
        # Checks if the letter is in the phrase.
        if letter in phrase:
            correct_letter = [x.start() for x in finditer(letter, phrase)]
            for y in correct_letter:
                encrypt_phrase = encrypt_phrase[:y] + encrypt_phrase[y].replace('*', letter) + encrypt_phrase[y+1:]
        else:
            i += 1
            num_guess -= 1
            print(f'Sorry, {letter} is not in the phrase.')
            print(f'You have {num_guess} guesses left.')
        
        # Check if the player wins or loses the match.
        winner = winner_check(num_guess, phrase, encrypt_phrase)
        if winner:
            break
        

def main():
    # Local variable for the number of rounds played that will be go up by 1 per round played.
    rounds_played = 0 
    
    # Player can define how many rounds to play.
    message = 'Enter how many rounds you want to play: '
    num_rounds = validate_input(message)
    
    # Will start the game here in respects to rounds played.
    while rounds_played != num_rounds:
        phrase = get_phrase()
        encrypt_phrase = get_encrypt_phrase(phrase)
        game_on(phrase, encrypt_phrase)
        rounds_played += 1
        
    

if __name__ == '__main__':
    main()
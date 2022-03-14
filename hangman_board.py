# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 12:49:41 2021

@author: Will Lacey
"""
from enum import Enum

class Board(Enum):
    
    HANGMAN = ['''
                    
   +---+
       |
       |
       |
      ===''', '''
      
   +---+
   O   |
       |
       |
      ===''', '''
      
   +---+
   O   |
   |   |
       |
      ===''', '''
      
   +---+
   O   |
  /|   |
       |
      ===''', '''
      
   +---+
   O   |
  /|\  |
       |
      ===''', '''
      
   +---+
   O   |
  /|\  |
  /    |
      ===''', '''
      
   +---+
   O   |
  /|\  |
  / \  |
      ===''']

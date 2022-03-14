# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 14:17:20 2021

@author: Will
"""

from random import shuffle

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
          'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

class Card(): 
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + " of " + self.suit
    
class Deck():
    
    def __init__(self):
        
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)
    
    def shuffle(self):
        shuffle(self.all_cards)
        
    def deal_one(self):
        return self.all_cards.pop()
    
class Player():
    
    # Each player has a name and starts with an empty hand.
    def __init__(self, name):
        
        self.name = name
        self.all_cards = []
        
    def remove_one(self):
        return self.all_cards.pop(0)
    
    # Can add a list of card objects or one card object.
    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards_.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'
    
# Game Setup.
player_one = Player('One')
player_two = Player('Two')

new_deck = Deck()
new_deck.shuffle()

# Now to split the deck in half.
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())
    
game_on = True

round_num = 0

while game_on:
    # Will be able to see how many rounds are needed to play the matches.
    round_num += 1
    print(f'Round {round_num}')
    
    # Check to see if player is out of cards.
    if len(player_one.all_cards) == 0:
        print('Player One, out of cards. Player Two wins.')
        game_one = False
        break
    
    if len(player_two.all_cards) == 0:
        print('Player Two, out of cards. Player One wins.')
        game_one = False
        break
    
    # Start a new round. Will append each players' all_cards hand (i.e., grab a single card and remove it).
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())
    
    at_war = True
    
    while at_war:
        
        # Player One won.
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False
        
        # Player Two won.
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_war = False
        
        # I-DE-CLARE-WAR
        else:
            print('WAR!')
            
            if len(player_one.all_cards) < 3:
                print('Player One unable to declare war.')
                print('Player Two wins.')
                game_on = False
                
            elif len(player_two.all_cards) < 3:
                print('Player Two unable to declare war.')
                print('Player One wins.')
                game_on = False
            
            else:
                for num in range(3):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())

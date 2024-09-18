import os
import colorama
from colorama import Back

colorama.init(autoreset=True)


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        
    def __str__(self):
        return f"{self.suit} {self.value}"


class Deck:
    def __init__(self, cards=None):
        if cards is None:
            cards = []
        self.cards = cards


    def show_cards(self): 
        for card in self.cards:
            print(card)


    def draw_card(self, index):
        self.cards.pop(index)


    @staticmethod
    def create_deck():  
        cards = [] 
        suits = ["♠", "♥", "♣", "♦"]
        values = ["Ess", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
        
        for suit in range(len(suits)):
            current_suit = suits[suit] 

            for value in range(len(values)):
                current_value = values[value]
                cards.append(Card(current_suit, current_value))
        
        return cards

os.system("cls")

cards = Deck().create_deck()

deck = Deck(cards)
deck.draw_card(2)
deck.show_cards()



#BALCKJACKGAME USING PYTHON

import random
"""             BLACKJACK - CARD CLASS                  """
""" 
The Card class represents a single card in the deck. It has two attributes: suit and rank. The __str__ method returns a string representation of the card, e.g., "Ace of Hearts".
"""
class Card:
    def __init__(self, suit, rank):
        # Initialize a Card object with a suit and rank
        self.suit = suit
        self.rank = rank

    def __str__(self):
        # Return a string representation of the card (e.g. "Ace of Hearts")
        return f"{self.rank['rank']} of {self.suit}"
"""             BLACKJACK - DECK CLASS             """

"""
The Deck class represents a deck of cards. It has a list of Card objects, which are created in the __init__ method. The shuffle method shuffles the deck, and the deal method deals a specified number of cards from the top of the deck.
"""
class Deck:
    def __init__(self):
        # Initialize a Deck object with an empty list of cards
        self.cards = []
        suits = ["spades", "clubs", "hearts", "diamonds"]
        ranks = [
            {"rank": "A", "value": 11},
            {"rank": "2", "value": 2},
            ...
        ]
        # Create a list of Card objects for each suit and rank
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        # Shuffle the deck of cards
        if len(self.cards) > 1:
            random.shuffle(self.cards)

    def deal(self, number):
        # Deal a specified number of cards from the top of the deck
        cards_dealt = []
        for x in range(number):
            if len(self.cards) > 0:
                card = self.cards.pop()
                cards_dealt.append(card)
        return cards_dealt
"""card1 = Card("hearts",{"rank": "j" , "value": 10})
print(card1)
deck1 = Deck()
deck2 = Deck()
deck2.shuffle()
print(deck1.cards)
print(deck2.cards)"""

"""             BLACKJACK - HARD CLASS                  """
"""
The Hand class represents a player's hand or the dealer's hand. It has a list of Card objects, a value attribute to store the total value of the hand, and a dealer attribute to indicate whether it's the dealer's hand. The add_card method adds cards to the hand, calculate_value calculates the total value of the hand, get_value returns the total value, is_blackjack checks if the hand is a blackjack, and display prints the hand.
"""
class Hand:
    def __init__(self, dealer=False):
        # Initialize a Hand object with an empty list of cards and a dealer flag
        self.cards = []
        self.value = 0
        self.dealer = dealer

    def add_card(self, card_list):
        # Add cards to the hand
        self.cards.extend(card_list)

    def calculate_value(self):
        # Calculate the total value of the hand
        self.value = 0
        has_ace = False
        for card in self.cards:
            card_value = int(card.rank["value"])
            self.value += card_value
            if card.rank["rank"] == "A":
                has_ace = True
        if has_ace and self.value > 21:
            self.value -= 10

    def get_value(self):
        # Return the total value of the hand
        self.calculate_value()
        return self.value

    def is_blackjack(self):
        # Check if the hand is a blackjack (value of 21)
        return self.get_value() == 21

    def display(self, show_all_dealer_cards=False):
        # Display the hand
        print(f'''{"Dealer's" if self.dealer else "Your"} Hand:''')
        for index, card in enumerate(self.cards):
            if index == 0 and self.dealer and not show_all_dealer_cards and not self.is_blackjack():
                print("hidden")
            else:
                print(card)
        if not self.dealer:
            print("Value:", self.get_value())
        print()
"""    
deck = Deck()
deck.shuffle()

hand = Hand()
hand.add_card(deck.deal(2))
hand.display()
"""
class Game:
    def play(self):
        game_number = 0
        games_to_play = 0

        while games_to_play <= 0:
            try:
                games_to_play = int(input("How many games do you want to play ?\n "))
            except:
                print("You must enter a number.")

        while game_number < games_to_play:
            game_number += 1

            deck = Deck()
            deck.shuffle()

            player_hand = Hand()
            dealer_hand = Hand(dealer=True)

            for i in range(2):
                player_hand.add_card(deck.deal(1))
                dealer_hand.add_card(deck.deal(1))

            print()
            print("*" * 30)
            print(f"Game {game_number} of {games_to_play}")
            print("*" * 30)
            player_hand.display()
            dealer_hand.display()

            if self.check_winner(player_hand, dealer_hand):
                continue

            choice = ""
            while player_hand.get_value() < 21 and choice not in ["s" , "stand"] :
                choice = input("Please choose 'Hit' or 'Stand' :").lower()
                print()
                while choice not in ["h" , "s","hit","stand"]:
                    choice  = input("please enter 'Hit' or 'stand': ").lower()
                    print()
                if choice in ["hit","h"]:
                    player_hand.add_card(deck.deal(1))
                    player_hand.display()
                    
            if self.check_winner(player_hand, dealer_hand):
                continue

            player_hand_value = player_hand.get_value()
            dealer_hand_value = dealer_hand.get_value()

            while dealer_hand_value < 17:
                dealer_hand.add_card(deck.deal(1))
                dealer_hand_value = dealer_hand.get_value()


            dealer_hand.display(show_all_dealer_cards=True)

            if self.check_winner(player_hand, dealer_hand):
                continue

            print("Final Results")
            print("Your hand:", player_hand_value)
            print("Dealer's hand:",dealer_hand_value)

            self.check_winner(player_hand,dealer_hand, True)

        print("\nThanks for playing !")
    
    def check_winner(self ,player_hand, dealer_hand ,game_over=False):
            if not game_over:
                if player_hand.get_value() > 21:
                    print("You busted. Dealer wins! ")
                    return True
                elif dealer_hand.get_value() > 21:
                    print("Dealer busted. You wins! ")
                    return True
                elif dealer_hand.is_blackjack() and player_hand.is_blackjack():
                    print("Both player have blackjack! Tie ! ")
                    return True
                elif player_hand.is_blackjack():
                    print("You have blackjack . You Win! ")
                    return True
                elif dealer_hand.is_blackjack():
                    print("Dealer has blackjack. dealer wins!")
                    return True
            else:
                if player_hand.get_value() > dealer_hand.get_value():
                    print("You Win!")
                elif player_hand.get_value() == dealer_hand.get_value():
                    print("You Tie ")
                else:
                    print("Dealer wins !")
                return True
            return False
g = Game()
g.play()
        






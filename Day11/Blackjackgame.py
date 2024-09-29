#BALCKJACKGAME USING PYTHON

import random

cards = []
suits = ["spades","clubs","hearts","diamonds"]
ranks = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
for suit in suits:
    for rank in ranks:
        cards.append([suit , rank])


def shuffle():
    random.shuffle(cards)
def deal(number):
    cards_dealt = []
    for x in range(number):
        card = cards.pop()
        cards_dealt.append(card)
    return cards_dealt

#print(cards)
"""
RESULT=

[['hearts', 'J'], ['diamonds', '2'], ['clubs', '3'], ['diamonds', '3'],
['diamonds', 'K'], ['spades', 'Q'], ['clubs', '5'], ['clubs', '8'], ['hearts', '6']
, ['hearts', '10'], ['diamonds', '9'], ['diamonds', '6'], ['hearts', '3'],
['clubs', 'K'], ['spades', 'K'], ['spades', '10'], ['spades', '2'], ['spades', '9'],
['spades', '7'], ['diamonds', 'Q'], ['diamonds', '8'], ['spades', 'A'], ['clubs', '2'],
['clubs', '10'], ['diamonds', 'J'], ['hearts', '7'], ['diamonds', '4'], ['spades', '8'],
['clubs', 'A'], ['spades', '5'], ['clubs', '7'], ['diamonds', '10'], ['diamonds', '5'],
['spades', 'J'], ['hearts', '4'], ['diamonds', '7'], ['clubs', '9'], ['hearts', '5'],
['clubs', 'Q'], ['hearts', 'Q'], ['clubs', '4'], ['diamonds', 'A'], ['hearts', 'A'],
['spades', '3'], ['hearts', '2'], ['spades', '6'], ['hearts', '8'], ['clubs', 'J'],
['hearts', '9'], ['spades', '4'], ['hearts', 'K'], ['clubs', '6']]
"""

#print(card)
#result = ['spades', '3']

shuffle()

cards_dealt= deal(2)

card = cards_dealt[0]
rank = card[1]

if rank == "A":
    value = 11
elif rank == "J" or rank == "Q" or rank == "K":
    value = 10
else:
    value = rank

rank_dict = {"rank":rank , "value":value}

print(rank ,value)
"""START AT 3:45:54"""


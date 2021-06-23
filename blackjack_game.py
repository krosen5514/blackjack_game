print('Welcome to Blackjack, thanks for playing')
print('----------------------------------------')
print('Shuffle up and deal!')
print('----------------------------------------')

#using an API get request to import 6 decks of cards
#import requests
#shuffleurl='https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=6'
#resp_shuffle=requests.get(shuffleurl)
#deck=resp_shuffle.json()
#deck_id= deck["deck_id"]

#using a post API to draw from the deck
#drawurl= f'https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count={2}'
#resp_draw=requests.post(drawurl)
#print(resp_draw.status_code)
#cards_drawn=resp_draw.json()
#print(cards_drawn)

#assigning a player and a dealer
#player()
#dealer()

#if cards_drawn["cards"][0]["value"]:
    #print(cards_drawn["cards"][0]["value"])

#inputdict[key] = newvalue

#or using a dictionary defined within the code
deck = [
    {"id" : 1, "suit": 'clubs', "card": 'Ace',"value": 11},
    {"id" : 2, "suit": 'clubs', "card": '2', "value": 2 },
    {"id" : 3, "suit": 'clubs', "card": '3', "value": 3 },
    {"id" : 4, "suit": 'clubs', "card": '4', "value": 4 },
    {"id" : 5, "suit": 'clubs', "card": '5', "value": 5 },
    {"id" : 6, "suit": 'clubs', "card": '6', "value": 6 },
    {"id" : 7, "suit": 'clubs', "card": '7', "value": 7 },
    {"id" : 8, "suit": 'clubs', "card": '8', "value": 8 },
    {"id" : 9, "suit": 'clubs', "card": '9', "value": 9 },
    {"id" : 10, "suit": 'clubs', "card": '10', "value": 10 },
    {"id" : 11, "suit": 'clubs', "card": 'Jack', "value": 10 },
    {"id" : 12, "suit": 'clubs', "card": 'Queen', "value": 10 },
    {"id" : 13, "suit": 'clubs', "card": 'King', "value": 10 },

     {"id" : 14, "suit": 'diamonds', "card": 'Ace', "value": 11},
     {"id" : 15, "suit": 'diamonds', "card": '2', "value": 2 },
     {"id" : 16, "suit": 'diamonds', "card": '3', "value": 3 },
     {"id" : 17, "suit": 'diamonds', "card": '4', "value": 4 },
     {"id" : 18, "suit": 'diamonds', "card": '5', "value": 5 },
     {"id" : 19, "suit": 'diamonds', "card": '6', "value": 6 },
     {"id" : 20, "suit": 'diamonds', "card": '7', "value": 7 },
     {"id" : 21, "suit": 'diamonds', "card": '8', "value": 8 },
     {"id" : 22, "suit": 'diamonds', "card": '9', "value": 9 },
     {"id" : 23, "suit": 'diamonds', "card": '10', "value": 10 },
     {"id" : 24, "suit": 'diamonds', "card": 'Jack', "value": 10 },
     {"id" : 25, "suit": 'diamonds', "card": 'Queen', "value": 10 },
     {"id" : 26, "suit": 'diamonds', "card": 'King', "value": 10 },

     {"id" : 27, "suit": 'hearts', "card": 'Ace', "value": 11},
     {"id" : 28, "suit": 'hearts', "card": '2', "value": 2 },
     {"id" : 29, "suit": 'hearts', "card": '3', "value": 3 },
     {"id" : 30, "suit": 'hearts', "card": '4', "value": 4 },
     {"id" : 31, "suit": 'hearts', "card": '5', "value": 5 },
     {"id" : 32, "suit": 'hearts', "card": '6', "value": 6 },
     {"id" : 33, "suit": 'hearts', "card": '7', "value": 7 },
     {"id" : 34, "suit": 'hearts', "card": '8', "value": 8 },
     {"id" : 35, "suit": 'hearts', "card": '9', "value": 9 },
     {"id" : 36, "suit": 'hearts', "card": '10', "value": 10 },
     {"id" : 37, "suit": 'hearts', "card": 'Jack', "value": 10 },
     {"id" : 38, "suit": 'hearts', "card": 'Queen', "value": 10 },
     {"id" : 39, "suit": 'hearts', "card": 'King', "value": 10 },

     {"id" : 40, "suit": 'spades', "card": 'Ace', "value": 11},
     {"id" : 41, "suit": 'spades', "card": '2', "value": 2 },
     {"id" : 42, "suit": 'spades', "card": '3', "value": 3 },
     {"id" : 43, "suit": 'spades', "card": '4', "value": 4 },
     {"id" : 44, "suit": 'spades', "card": '5', "value": 5 },
     {"id" : 45, "suit": 'spades', "card": '6', "value": 6 },
     {"id" : 46, "suit": 'spades', "card": '7', "value": 7 },
     {"id" : 47, "suit": 'spades', "card": '8', "value": 8 },
     {"id" : 48, "suit": 'spades', "card": '9', "value": 9 },
     {"id" : 49, "suit": 'spades', "card": '10', "value": 10 },
     {"id" : 50, "suit": 'spades', "card": 'Jack', "value": 10 },
     {"id" : 51, "suit": 'spades', "card": 'Queen', "value": 10 },
     {"id" : 52, "suit": 'spades', "card": 'King', "value": 10 }
]

import random
from pprint import pprint

active_deck = deck
# pprint(len(deck2))

# last_draw = random.choice(deck2)
# deck2 = [i for i in deck2 if not (i["id"] == last_draw["id"])]
# pprint(len(deck2))



# ROUND 1 | ROUND 1 | ROUND 1 | ROUND 1 | ROUND 1 | ROUND 1 | ROUND 1 | ROUND 1 | ROUND 1 | 

#Player drawing cards
# last_draw = random.choice(deck2)
# deck2 = [i for i in deck2 if not (i["id"] == last_draw["id"])]
# player_hand = last_draw
# player_score = last_draw["value"]


player_card1 = random.choice(deck)
active_deck = [i for i in active_deck if not (i["id"] == player_card1["id"])]

player_card2 = random.choice(deck)
active_deck = [i for i in active_deck if not (i["id"] == player_card2["id"])]


print(f"       Draw 1: {player_card1['card']} of {player_card1['suit']}")
print(f"       Draw 2: {player_card2['card']} of {player_card2['suit']}")

#Getting an initial score for the player
player_score = (player_card1["value"] + player_card2["value"])
print(f"Current total: {player_score}")
print()


# Giving the player blackjack
# if player_score == 21:
#     print('Blackjack! Nice job')
#     exit


# Giving the dealer cards
dealer_card1 = random.choice(deck)
active_deck = [i for i in active_deck if not (i["id"] == dealer_card1["id"])]

dealer_card2 = random.choice(deck)
active_deck = [i for i in active_deck if not (i["id"] == dealer_card2["id"])]

print(f"The Dealer Drew: {dealer_card1['card']} of {dealer_card1['suit']}")
dealer_score = (dealer_card1['value']+dealer_card2['value'])
print(f"   Dealer Total: {dealer_card1['value']} + ?")
print()


# Dealer gets blackjack
# if dealer_score == 21:
#     print('Dealer has Blackjack... sorry...')
#     exit


# DECISION ROUNDS | DECISION ROUNDS | DECISION ROUNDS | DECISION ROUNDS | DECISION ROUNDS |

#Hit or stay, this will be a while loop
round = 2

while True:
    player_action = input("Would you like to HIT or STAY? ")

    if player_action.upper() == ("HIT"):
        
        round += 1
        player_card = random.choice(active_deck)
        active_deck = [i for i in active_deck if not (i["id"] == player_card["id"])]

        print(f"       Draw {round}: {player_card['card']} of {player_card['suit']}")
        player_score += player_card['value']
        print(f"      Current Total: {player_score}")
        print()

    elif player_action.upper() == ("STAY"):
        print("Game ends")
        break

    else:
        print("Invalid input, try again!")




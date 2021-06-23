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
deck=[
    {"suit": 'clubs', "card": 'Ace',"value": 11},
    {"suit": 'clubs', "card": '2', "value": 2 },
    {"suit": 'clubs', "card": '3', "value": 3 },
    {"suit": 'clubs', "card": '4', "value": 4 },
    {"suit": 'clubs', "card": '5', "value": 5 },
    {"suit": 'clubs', "card": '6', "value": 6 },
    {"suit": 'clubs', "card": '7', "value": 7 },
    {"suit": 'clubs', "card": '8', "value": 8 },
    {"suit": 'clubs', "card": '9', "value": 9 },
    {"suit": 'clubs', "card": '10', "value": 10 },
    {"suit": 'clubs', "card": 'Jack', "value": 10 },
    {"suit": 'clubs', "card": 'Queen', "value": 10 },
    {"suit": 'clubs', "card": 'King', "value": 10 },

     {"suit": 'diamonds', "card": 'Ace', "value": 11},
     {"suit": 'diamonds', "card": '2', "value": 2 },
     {"suit": 'diamonds', "card": '3', "value": 3 },
     {"suit": 'diamonds', "card": '4', "value": 4 },
     {"suit": 'diamonds', "card": '5', "value": 5 },
     {"suit": 'diamonds', "card": '6', "value": 6 },
     {"suit": 'diamonds', "card": '7', "value": 7 },
     {"suit": 'diamonds', "card": '8', "value": 8 },
     {"suit": 'diamonds', "card": '9', "value": 9 },
     {"suit": 'diamonds', "card": '10', "value": 10 },
     {"suit": 'diamonds', "card": 'Jack', "value": 10 },
     {"suit": 'diamonds', "card": 'Queen', "value": 10 },
     {"suit": 'diamonds', "card": 'King', "value": 10 },

     {"suit": 'hearts', "card": 'Ace', "value": 11},
     {"suit": 'hearts', "card": '2', "value": 2 },
     {"suit": 'hearts', "card": '3', "value": 3 },
     {"suit": 'hearts', "card": '4', "value": 4 },
     {"suit": 'hearts', "card": '5', "value": 5 },
     {"suit": 'hearts', "card": '6', "value": 6 },
     {"suit": 'hearts', "card": '7', "value": 7 },
     {"suit": 'hearts', "card": '8', "value": 8 },
     {"suit": 'hearts', "card": '9', "value": 9 },
     {"suit": 'hearts', "card": '10', "value": 10 },
     {"suit": 'hearts', "card": 'Jack', "value": 10 },
     {"suit": 'hearts', "card": 'Queen', "value": 10 },
     {"suit": 'hearts', "card": 'King', "value": 10 },

     {"suit": 'spades', "card": 'Ace', "value": 11},
     {"suit": 'spades', "card": '2', "value": 2 },
     {"suit": 'spades', "card": '3', "value": 3 },
     {"suit": 'spades', "card": '4', "value": 4 },
     {"suit": 'spades', "card": '5', "value": 5 },
     {"suit": 'spades', "card": '6', "value": 6 },
     {"suit": 'spades', "card": '7', "value": 7 },
     {"suit": 'spades', "card": '8', "value": 8 },
     {"suit": 'spades', "card": '9', "value": 9 },
     {"suit": 'spades', "card": '10', "value": 10 },
     {"suit": 'spades', "card": 'Jack', "value": 10 },
     {"suit": 'spades', "card": 'Queen', "value": 10 },
     {"suit": 'spades', "card": 'King', "value": 10 }
]
import random
#Point values dict
#player_hand=()

#Player drawing cards
player_card1=random.choice(deck)
player_card2=random.choice(deck)
print('You Drew:', player_card1["card"], "of", player_card1["suit"], "and", player_card2["card"], "of", player_card2["suit"])

#Getting an initial score for the player
player_score1=0
player_score1=(player_card1["value"]+player_card2["value"])

#Giving the player blackjack
if player_score1 == 21:
    print('Blackjack! Nice job')

#Giving the dealer cards
dealer_card1=random.choice(deck)
dealer_card2=random.choice(deck)
print('The Dealer Drew:', dealer_card1["card"], "of", dealer_card1["suit"])
dealer_score1=(dealer_card1["value"]+dealer_card2["value"])

#Dealer gets blackjack
if dealer_score1 == 21:
    print('Dealer has Blackjack... sorry...')

#Hit or stay, this will be a while loop

player_action= input("Would you like to HIT or STAY?")

if player_action.upper() == ("HIT"):
    player_card3=random.choice(deck)
    print('You Drew:', player_card3["card"], "of", player_card3["suit"])
elif player_action.upper() == ("STAY"):
    print("Game ends")
else:
    print("Invalid input, try again!")

player_score2=(player_card1["value"]+player_card2["value"]+player_card3["value"])


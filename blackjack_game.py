print()
print("----------------------------------------")
print("Welcome to Blackjack")
print("----------------------------------------")
print("Shuffle up and deal!")
print("----------------------------------------")
print()

from pandas import read_csv

while True:
    deck_count = input("How many decks would you like to play with (Min=1, Max=6): ")
    if deck_count == "1" or "2" or "3" or "4" or "5" or "6":
        filepath_csv = f"data/{deck_count}decks.csv"
        print(filepath_csv)
        break
    else:
        print("Invalid input, please enter 1, 2, 3, 4, 5, or 6")
    
deck_df = read_csv(filepath_csv)
active_deck = deck_df.to_dict("records")


# ROUND 1 | ROUND 1 | ROUND 1 | ROUND 1 | ROUND 1 | ROUND 1 | ROUND 1 | ROUND 1 | ROUND 1 | 

import random
from pprint import pprint

# Player is delt first card
player_card1 = random.choice(active_deck)
active_deck = [i for i in active_deck if not (i["id"] == player_card1["id"])]
print(f"       Draw 1: {player_card1['card']} of {player_card1['suit']}")
# print("Cards remaining in deck:",len(active_deck))


# Player is delt second card
player_card2 = random.choice(active_deck)
active_deck = [i for i in active_deck if not (i["id"] == player_card2["id"])]
print(f"       Draw 2: {player_card2['card']} of {player_card2['suit']}")

# Player initial score
player_score = (player_card1["value"] + player_card2["value"])
print(f"        Total: {player_score}")
print()

if player_score == 21:
    print('Instant blackjack, you WIN!')
    exit


# Giving the dealer cards
dealer_card1 = random.choice(deck)
active_deck = [i for i in active_deck if not (i["id"] == dealer_card1["id"])]

dealer_card2 = random.choice(deck)
active_deck = [i for i in active_deck if not (i["id"] == dealer_card2["id"])]

print(f"  Dealer Draw: {dealer_card1['card']} of {dealer_card1['suit']}")
dealer_score = (dealer_card1['value']+dealer_card2['value'])
print(f" Dealer Total: {dealer_card1['value']} + ???")
print()


# Dealer gets blackjack
if dealer_score == 21:
    print('Dealer has Blackjack... sorry...')
    exit


# DECISION ROUNDS | DECISION ROUNDS | DECISION ROUNDS | DECISION ROUNDS | DECISION ROUNDS |

#Hit or stay, this will be a while loop
round = 2

while True:
    player_action = input("HIT or STAY? ")
    print()
    if player_action.upper() == ("HIT"):
        
        round += 1
        player_card = random.choice(active_deck)
        active_deck = [i for i in active_deck if not (i["id"] == player_card["id"])]

        print(f"       Draw {round}: {player_card['card']} of {player_card['suit']}")
        player_score += player_card['value']
        print(f"        Total: {player_score}")
        print()

        if player_score > 21:
            print("BUST! SORRY!")
            break

    elif player_action.upper() == ("STAY"):
        print("Game ends")
        break

    else:
        print("Invalid input, please enter 'HIT' or 'STAY'")




from pandas import read_csv
import random
from pprint import pprint
import dotenv
import os
dotenv.load_dotenv()
PLAYER_NAME = os.getenv("PLAYER_NAME")


print()
print("----------------------------------------")
print(f"Welcome to Blackjack, {PLAYER_NAME}!")
print("----------------------------------------")
print("Shuffle up and deal!")
print("----------------------------------------")
print()


# NEW FROM PROFESSOR
def draw_a_card(deck):
    card = random.choice(deck)
    deck = [i for i in deck if not (i["id"] == card["id"])]
    return card, deck


valid_decks = ["1", "2", "3", "4", "5", "6"]

while True:
    deck_count = input("How many decks would you like to play with (Min=1, Max=6): ")
    if deck_count in valid_decks:
    # if deck_count == "1" or "2" or "3" or "4" or "5" or "6":
        filepath_csv = f"data/{deck_count}decks.csv"
        break
    else:
        print("Invalid input, please enter 1, 2, 3, 4, 5, or 6")


deck_df = read_csv(filepath_csv)
active_deck = deck_df.to_dict("records")



# ROUND 1 | ROUND 1 | ROUND 1 | ROUND 1 | ROUND 1 | ROUND 1 | ROUND 1 | ROUND 1 | ROUND 1 | 


while True:
    
    # Player is delt first card
    print()
    player_card1, active_deck = draw_a_card(active_deck)
    print(f"       Draw 1: {player_card1['card']} of {player_card1['suit']}")

    # Player is delt second card
    player_card2, active_deck = draw_a_card(active_deck)
    print(f"       Draw 2: {player_card2['card']} of {player_card2['suit']}")


    # Player initial score
    player_score = (player_card1["value"] + player_card2["value"])
    print(f"        Total: {player_score}")
    print()

    if player_score == 21:
        print('Instant blackjack, you WIN! Walk away now!!!')
        print()
        while True:
            walk = input("Would you like to walk (Y or N)? ")
            print()
            if walk == "Y":
                print("Good move.")
                exit()
            elif walk == "N":
                break


    # Giving the dealer cards
    dealer_card1, active_deck = draw_a_card(active_deck)
    dealer_card2, active_deck = draw_a_card(active_deck)

    print(f"Dealer Draw 1: {dealer_card1['card']} of {dealer_card1['suit']}")
    print(f"Dealer Draw 2: CARD IS FACED DOWN")
    dealer_score = (dealer_card1['value'] + dealer_card2['value'])
    print(f" Dealer Total: {dealer_card1['value']} + ??? = ???")
    print()

    # Dealer gets blackjack
    if dealer_score == 21:
        print('Dealer has Blackjack... sorry...')
        print()
        exit()


    # DECISION ROUNDS | DECISION ROUNDS | DECISION ROUNDS | DECISION ROUNDS | DECISION ROUNDS |

    #Hit or stay, this will be a while loop
    round_player = 2
    round_dealer = 2

    while True:
        player_action = input("HIT or STAY? ")
        print()
        if player_action.upper() == ("HIT"):
            
            round_player += 1        
            player_card, active_deck = draw_a_card(active_deck)

            print(f"       Draw {round_player}: {player_card['card']} of {player_card['suit']}")
            player_score += player_card['value']
            print(f"        Total: {player_score}")
            print()

            if player_score > 21:
                print(f"               {player_score} > 21 ... BUST! SORRY!")
                print()
                break

        elif player_action.upper() == ("STAY"):
            print(f"           ... DEALER'S FACED DOWN CARD IS FLIPPING UP ...")
            print()
            print(f"Dealer Draw 2: {dealer_card2['card']} of {dealer_card2['suit']}")
            print(f" Dealer Total: {dealer_card1['value']} + {dealer_card2['value']} = {dealer_score}")
            print()

            while True:
                if dealer_score < 17:
                    print(f"The dealer must reach a soft 17.")
                    
                    round_dealer += 1               
                    dealer_card, active_deck = draw_a_card(active_deck)
                    print(f"Dealer Draw {round_dealer}: {dealer_card['card']} of {dealer_card['suit']}")
                    dealer_score += dealer_card['value']
                    print(f" Dealer Total: {dealer_score}")

                    print()

                elif dealer_score > 21:
                    print(f"Dealer BUSTED - you WIN!")
                    print()
                    break

                else:
                    if player_score > dealer_score:
                        print(f"{player_score} is better than {dealer_score} - you WIN this hand!")
                        print("Congratulations! Keep the winning streak going!")
                        print()
                        break
                    elif player_score == dealer_score:
                        print(f"{player_score} = {dealer_score} - PUSH.")
                        print("Feel free to try again.")
                        print()
                        break
                    else:
                        print(f"{player_score} is worse than {dealer_score} - you LOSE this hand.")
                        print("Sorry! Please try again.")
                        print()
                        break
            
            break

        else:
            print("Invalid input, please enter 'HIT' or 'STAY'")

    while True:
        print(f"There are {len(active_deck)} cards left in the deck.")
        play_again = input("Would you like to play again (Y or N)? ")
        
        
        
        
        if play_again.upper() == "Y" and len(active_deck > 22):
            print()
            print("Good move - the deck is hot!")
            break            
        elif play_again.upper() == "Y" and len(active_deck < 23):
            print()
            print("The dealer is runing low on cards and they need to reshuffle the deck")
            print("Please play again")
            exit()
        elif play_again.upper() == "N":
            print("Thanks for playing.")
            exit()
        else:
            print("Sorry invlaid input. Please enter 'Y' or 'N': ")




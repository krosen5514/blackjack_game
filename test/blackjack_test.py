import random
from app.blackjack_game import draw_a_card

deck= [
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
     {"id" : 15, "suit": 'diamonds', "card": '2', "value": 2 }
]

def test_draw_a_card():
    deck=[
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
     {"id" : 15, "suit": 'diamonds', "card": '2', "value": 2 }

]
# def test_draw_a_card():
#     result = draw_a_card(deck)
#     assert result == print(random.choice(deck))

card , deck = draw_a_card(deck)

#assert that the card is a dictionary and that it has certain keys we expect it to have
print(type(card))
print(card["id"])
#count the number of remaining cards in active deck.
#assert that len is 1 less than deck was to start with to ensure we're removing a card from the deck
#indented within the test function
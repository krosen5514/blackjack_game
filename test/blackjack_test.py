from app.blackjack_game import draw_a_card


def test_draw_a_card():
    
    deck = [
    {"id" : 1, "suit": 'clubs', "card": 'Ace',"value": 11},
    {"id" : 2, "suit": 'clubs', "card": '2', "value": 2 },
    {"id" : 3, "suit": 'clubs', "card": '3', "value": 3 },
    ]
    
    assert type(deck) == list

    # assert that the card is a dectionary and that it has certain keys we expect it to have
    card = deck[0]
    assert type(card) == dict
    assert card["id"] == 1
    assert card["suit"] == 'clubs'
    assert card["card"] == 'Ace'
    assert card["value"] == 11

    # count the number of remaining cards in active deck
    remaining_cards = len(deck)
    assert remaining_cards == 3

    # assert that len is 1 less than deck was to start with to ensure we're removing a card from the deck
    card, deck = draw_a_card(deck)
    remaining_cards = len(deck)
    assert remaining_cards == 2

    card, deck = draw_a_card(deck)
    remaining_cards = len(deck)
    assert remaining_cards == 1

    # these assertions should be indented within the test function
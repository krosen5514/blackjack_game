from app.blackjack_game import draw_a_card


def test_draw_a_card():
    deck=[
        {2,"clubs",2,2,1},
        {3,"clubs",3,3,1},
        {4,"clubs",4,4,1},
        {5,"clubs",5,5,1},
        {6,"clubs",6,6,1},
        {7,"clubs",7,7,1},
        {8,"clubs",8,8,1},
        {9,"clubs",9,9,1},
        {10,"clubs",10,10,1}
    ]

    #deck is list of dictionaries
    #invoke draw card function 

card , active_deck = draw_a_card(deck)

#assert that the card is a dectionary and that it has certain keys we expect it to have
#count the number of remaining cards in active deck.
#assert that len is 1 less than deck was to start with to ensure we're removing a card from the deck
#indented within the test function
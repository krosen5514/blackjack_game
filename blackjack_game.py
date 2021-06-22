print('Welcome to Blackjack, thanks for playing')
print('----------------------------------------')
print('Shuffle up and deal!')
print('----------------------------------------')

#using an API get request to import 6 decks of cards
import requests
shuffleurl='https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=6'
resp_shuffle=requests.get(shuffleurl)
deck=resp_shuffle.json()
deck_id= deck["deck_id"]
print(deck_id)

#using a post API to draw from the deck
drawurl= f'https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=3'
resp_draw=requests.post(drawurl)
print(resp_draw.status_code)
cards_drawn=resp_draw.json()
print(cards_drawn)
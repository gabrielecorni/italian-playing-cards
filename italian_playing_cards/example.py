from core.decks import DeckFactory, DeckType, Deck
from core.cards import Card, Value, Suit
from typing import List
import random

if __name__ == "__main__":
    d: Deck = DeckFactory.get_by_country(DeckType.ITALIAN)
    print(f"Got a {d} with {len(d)} cards.")
    
    d.shuffle(10)
    print(f"{d} shuffled.")

    print(f"Used {d.idx} cards (empty={d.is_empty()}).")

    player_one_hand: List[Card] = d.draw(3)
    print(f"Player1 hand: {player_one_hand}.")
    player_two_hand: List[Card] = d.draw(3)
    print(f"Player2 hand: {player_two_hand}.")

    print(f"Used {d.idx} cards (empty={d.is_empty()}).")
    print("Start iterating...")

    for card in d.iterate():
        print(f"> Drawn {card}\t({d.idx} used, empty={d.is_empty()}).")

    print(f"{d} entirely used.")
#!/usr/bin/env python

from abc import ABC, abstractmethod
from typing import List, Iterable
from core.cards import Card, Value, Suit
import enum
import random


class DeckType(enum.Enum):
    ITALIAN = "\U0001f1ee"
    SPANISH = "\U0001f1ea"
    FRENCH  = "\U0001f1eb"
    GERMAN  = "\U0001f1e9"

class Deck(ABC):
    def __init__(self, n_wild_cards=0) -> None:
        super().__init__()
        self._cards: List[Card] = self._generate() + n_wild_cards * [Card(Value.JOKER, Suit.JOKER)]
        self.idx = 0

    def __len__(self):
        return len(self._cards)

    def __str__(self) -> str:
        return "Card Deck"

    def __repr__(self) -> str:
        return "Card Deck"

    @staticmethod
    @abstractmethod
    def _generate() -> List[Card]:
        pass

    def shuffle(self, n: int = 5) -> None:
        amount = max(n, 1)  # at least one time
        for _ in range(amount):
            random.shuffle(self._cards)

    def draw(self, n: int = 1) -> List[Card]:
        amount = min(n, self.__len__() - n)  # if less card in deck than requested, return the remaining ones
        drawn_cards = self._cards[self.idx:self.idx+amount]
        self.idx += amount
        return drawn_cards

    def is_empty(self) -> bool:
        return self.idx == self.__len__()

    def iterate(self) -> Iterable[Card]:
        for card in self._cards[self.idx:]:
            self.idx += 1
            yield card

class ItalianDeck(Deck):
    def __init__(self) -> None:
        super().__init__(n_wild_cards=0)

    @staticmethod
    def _generate() -> List[Card]:
        return [
            Card(v, s) 
            for v in [
                Value.ACE, 
                Value.TWO, 
                Value.THREE, 
                Value.FOUR, 
                Value.FIVE, 
                Value.SIX, 
                Value.SEVEN, 
                Value.KNAVE, 
                Value.KNIGHT, 
                Value.KING
            ]
            for s in [
                Suit.SWORDS,
                Suit.CUPS,
                Suit.COINS,
                Suit.BATONS
            ]
        ]

    def __str__(self) -> str:
        return f"Italian {super().__str__()}"

    def __repr__(self) -> str:
        return f"Italian {super().__repr__()}"

class SpanishDeck(Deck):
    def __init__(self) -> None:
        super().__init__(n_wild_cards=0)

    @staticmethod
    def _generate() -> List[Card]:
        return [
            Card(v, s) 
            for v in [
                Value.ACE, 
                Value.TWO, 
                Value.THREE, 
                Value.FOUR, 
                Value.FIVE, 
                Value.SIX, 
                Value.SEVEN, 
                Value.EIGHT,
                Value.NINE,
                Value.TEN,
                Value.KNAVE, 
                Value.KNIGHT, 
                Value.KING
            ]
            for s in [
                Suit.SWORDS,
                Suit.CUPS,
                Suit.COINS,
                Suit.CLUBS
            ]
        ]

    def __str__(self) -> str:
        return f"Spanish {super().__str__()}"

    def __repr__(self) -> str:
        return f"Spanish {super().__repr__()}"

class FrenchDeck(Deck):
    def __init__(self) -> None:
        super().__init__(n_wild_cards=0)

    @staticmethod
    def _generate() -> List[Card]:
        return [
            Card(v, s) 
            for v in [
                Value.ACE, 
                Value.TWO, 
                Value.THREE, 
                Value.FOUR, 
                Value.FIVE, 
                Value.SIX, 
                Value.SEVEN, 
                Value.EIGHT, 
                Value.NINE, 
                Value.TEN,
                Value.JACK,
                Value.QUEEN,
                Value.KING
            ]
            for s in [
                Suit.HEARTS,
                Suit.SQUARES,
                Suit.FLOWERS,
                Suit.PIKES
            ]
        ]

    def __str__(self) -> str:
        return f"French {super().__str__()}"

    def __repr__(self) -> str:
        return f"French {super().__repr__()}"

class GermanDeck(Deck):
    def __init__(self) -> None:
        super().__init__(n_wild_cards=1)

    @staticmethod
    def _generate() -> List[Card]:
        return [
            Card(v, s) 
            for v in [
                Value.ACE, 
                Value.TWO, 
                Value.THREE, 
                Value.FOUR, 
                Value.FIVE, 
                Value.SIX, 
                Value.SEVEN, 
                Value.KNAVE, 
                Value.KNIGHT, 
                Value.KING
            ]
            for s in [
                Suit.ACORNS,
                Suit.BELLS,
                Suit.LEAVES,
                Suit.HEARTS
            ]
        ]

    def __str__(self) -> str:
        return f"German {super().__str__()}"

    def __repr__(self) -> str:
        return f"German {super().__repr__()}"

class DeckFactory(object):
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def get_by_country(kind: DeckType):
        return {
            DeckType.ITALIAN: ItalianDeck,
            DeckType.SPANISH: SpanishDeck,
            DeckType.FRENCH:  FrenchDeck,
            DeckType.GERMAN:  GermanDeck,
        }.get(kind)()
#!/usr/bin/env python
from collections import namedtuple
import enum

class Value(enum.Enum):
    ZERO   = "\U00000030"
    ONE    = "\U00000031"
    TWO    = "\U00000032"
    THREE  = "\U00000033"
    FOUR   = "\U00000034"
    FIVE   = "\U00000035"
    SIX    = "\U00000036" 
    SEVEN  = "\U00000037" 
    EIGHT  = "\U00000038"
    NINE   = "\U00000039" 
    TEN    = "\U0001f51f"
    KNAVE  = "\U0001f464"
    JACK   = "\U0001f464"
    KNIGHT = "\U0001f40e"
    QUEEN  = "\U0001f460"
    KING   = "\U0001f451"
    ACE    = "\U0001f3fa"
    JOKER  = "\U0001f921"

class Suit(enum.Enum):
    SWORDS  = "\U00002694"
    CUPS    = "\U0001f3c6"
    COINS   = "\U0001f4b0"
    CLUBS   = "\U0001f38b"
    BATONS  = "\U0001f334"
    HEARTS  = "\U00002665"
    SQUARES = "\U00002666"
    FLOWERS = "\U00002663"
    PIKES   = "\U00002660"
    ACORNS  = "\U0001f330"
    LEAVES  = "\U0001f343"
    BELLS   = "\U0001f514"
    JOKER   = "\U0001f921"

"""
A regular namedtuple would be enough, but in this case I wanted to redefine the native string representations.
They are __str__() and __repr__() methods.
To achieve that, just create a class inheriting from namedtuple, and redefine these methods.
=======
NOTE:
=======
__slots__ is redefined as well because it is a memory saving technique.
By setting it to an empty tuple we make sure that instances of this class take the same amount of
memory of a regular tuple. 
Without the __slots__ entry, every instance requires its own dictionary (which is much bigger than a tuple).
"""

class Card(namedtuple("Card", ["value", "suit"])):
    __slots__ = ()

    def __str__(self):
        """
        The one invoked with: print(card) or print(str(card))
        :return: narrow string representation
        """
        return f"{self.value.value} {self.suit.value}"

    def __repr__(self):
        """
        The one invoked with: print(repr(card))
        :return: wide string representation
        """
        return f"{self.value} of {self.suit}"
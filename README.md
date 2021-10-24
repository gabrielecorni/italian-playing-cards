# italian-playing-cards
A pythonic implementation of Italian card decks.

Ref:
+ [Wikipedia page](https://en.wikipedia.org/wiki/Italian_playing_cards)
+ [Emoji](https://unicode.org/emoji/charts/full-emoji-list.html)

---

### Run locally

Create and enter virtual environment:
```shell
poetry shell
```

Run the example:
```shell
python italian_playing_cards/example.py
```

Log:
```shell
$ python italian_playing_cards/example.py

Got a Italian Card Deck with 40 cards.
Italian Card Deck shuffled.
Used 0 cards (empty=False).
Player1 hand: [Value.SIX of Suit.COINS, Value.FIVE of Suit.CUPS, Value.KING of Suit.COINS].
Player2 hand: [Value.SIX of Suit.SWORDS, Value.KNIGHT of Suit.SWORDS, Value.THREE of Suit.CUPS].
Used 6 cards (empty=False).
Start iterating...
> Drawn 🐎 💰   (7 used, empty=False).
> Drawn 6 🏆    (8 used, empty=False).
> Drawn 🏺 🌴   (9 used, empty=False).
> Drawn 👤 ⚔    (10 used, empty=False).
> Drawn 7 🌴    (11 used, empty=False).
> Drawn 👑 🌴   (12 used, empty=False).
> Drawn 2 ⚔     (13 used, empty=False).
> Drawn 🐎 🏆   (14 used, empty=False).
> Drawn 3 ⚔     (15 used, empty=False).
> Drawn 👤 💰   (16 used, empty=False).
> Drawn 2 🏆    (17 used, empty=False).
> Drawn 5 💰    (18 used, empty=False).
> Drawn 🐎 🌴   (19 used, empty=False).
> Drawn 5 ⚔     (20 used, empty=False).
> Drawn 👤 🌴   (21 used, empty=False).
> Drawn 👑 🏆   (22 used, empty=False).
> Drawn 🏺 🏆   (23 used, empty=False).
> Drawn 3 🌴    (24 used, empty=False).
> Drawn 👤 🏆   (25 used, empty=False).
> Drawn 4 🏆    (26 used, empty=False).
> Drawn 7 ⚔     (27 used, empty=False).
> Drawn 7 💰    (28 used, empty=False).
> Drawn 6 🌴    (29 used, empty=False).
> Drawn 4 ⚔     (30 used, empty=False).
> Drawn 🏺 💰   (31 used, empty=False).
> Drawn 5 🌴    (32 used, empty=False).
> Drawn 3 💰    (33 used, empty=False).
> Drawn 7 🏆    (34 used, empty=False).
> Drawn 4 🌴    (35 used, empty=False).
> Drawn 👑 ⚔    (36 used, empty=False).
> Drawn 🏺 ⚔    (37 used, empty=False).
> Drawn 4 💰    (38 used, empty=False).
> Drawn 2 💰    (39 used, empty=False).
> Drawn 2 🌴    (40 used, empty=True).
Italian Card Deck entirely used.
```

Exit the virtual environment:
```shell
exit
```
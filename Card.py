from functools import total_ordering

# Unicode symbols for the suits
SUIT_SYMBOLS = {"H": "♥", "D": "♦", "S": "♠", "C": "♣"}


@total_ordering
class Card:
    def __init__(self, value, suit):
        self.value = value  # 1-13 where Ace is 1, King is 13
        self.suit = suit  # 'H', 'D', 'S', 'C'
        self.color = "red" if (suit == "D" or suit == "H") else "black"

    def __repr__(self):
        value_str = self.value_str(self.value)

        suit_symbol = SUIT_SYMBOLS[self.suit]

        # Apply color using ANSI escape codes based on the suit.
        if self.color == "red":
            return "\033[91m" + f"{value_str}".ljust(2) + f"{suit_symbol}\033[0m"
        else:
            return "\033[90m" + f"{value_str}".ljust(2) + f"{suit_symbol}\033[0m"

    def __eq__(self, other):
        if isinstance(other, Card):
            return (self.value, self.suit) == (other.value, other.suit)
        return False

    def __lt__(self, other):
        if isinstance(other, Card):
            # Sort by value first, then by suit
            return (self.value, self.suit) < (other.value, other.suit)
        return False

    def __hash__(self):
        return hash((self.value, self.suit))

    @classmethod
    def value_str(cls, value):
        return (
            "A"
            if value == 1
            else (
                "J"
                if value == 11
                else ("Q" if value == 12 else "K" if value == 13 else str(value))
            )
        )

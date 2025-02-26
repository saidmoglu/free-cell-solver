from collections import Counter
import copy
from Card import SUIT_SYMBOLS, Card


class GameState:
    def __init__(
        self,
        tableau,
        foundation,
        temp_slots,
        max_value=13,
        num_piles=8,
        max_temp_slots=4,
    ):
        self.tableau = tableau  # A list of lists, where each sublist is a pile of cards in the tableau
        self.foundation = foundation  # A dictionary {suit: top_card_value}
        self.temp_slots = temp_slots  # A set for temp cards
        self.max_value = max_value  # 13 for a standard deck
        self.num_piles = num_piles  # Number of tableau piles, standard is 8
        self.max_temp_slots = max_temp_slots  # Number of temp slots, standard is 4

    def is_goal(self):
        """Check if the game is won, all cards in the foundation."""
        return all(v == self.max_value for v in self.foundation.values())

    def __repr__(self):
        return f"GameState(tableau={self.tableau}, foundation={self.foundation}, temp_slots={self.temp_slots})"

    def pretty_print(self):
        foundation_str = "Found: " + "".join(
            [
                f"\033[91m{SUIT_SYMBOLS[suit]}:{Card.value_str(self.foundation.get(suit, '')).ljust(3)}\033[0m"
                for suit in ["H", "D"]
            ]
        )
        foundation_str += "".join(
            [
                f"\033[90m{SUIT_SYMBOLS[suit]}:{Card.value_str(self.foundation.get(suit, '')).ljust(3)}\033[0m"
                for suit in ["S", "C"]
            ]
        )

        temp_slots_str = "Temp: " + " | ".join(
            [str(card) if card else "[] " for card in self.temp_slots]
        )

        max_pile_height = max(len(pile) for pile in self.tableau)

        tableau_str = ""
        for row in range(max_pile_height):
            row_str = []
            for pile in self.tableau:
                if row < len(pile):
                    row_str.append(str(pile[row]))
                else:
                    row_str.append("   ")  # Empty space for shorter piles
            tableau_str += "|".join(row_str) + "\n"
        tableau_num_str = " ".join([str(i).ljust(3) for i in range(self.num_piles)])
        return f"{temp_slots_str}   {foundation_str}\nTableau:\n{tableau_num_str}\n{tableau_str}"

    def print_tableau_as_test_case(self):
        print("TestCase(")
        print('values="""')
        for pile in self.tableau:
            print(" ".join(f"{card.value}" for card in pile))
        print('""",')
        print('suits="""')
        for pile in self.tableau:
            print("".join(f"{card.suit}" for card in pile))
        print('""",')
        print("),")

    def normalized_tableau(self):
        """Sort the tableau piles to ensure equivalent states have identical tableau representations."""
        return tuple(
            sorted(
                [tuple(pile) for pile in self.tableau],
                key=lambda pile: (
                    (pile[-1].value if pile else 0),
                    (pile[-1].suit if pile else ""),
                    [(card.value, card.suit) for card in pile],
                ),
            )
        )

    def __hash__(self):
        return hash(
            (
                self.normalized_tableau(),
                frozenset(self.temp_slots),
                tuple(self.foundation.items()),
            )
        )

    def __eq__(self, other):
        return (
            self.normalized_tableau() == other.normalized_tableau()
            and self.temp_slots == other.temp_slots
            and self.foundation == other.foundation
        )

    def validate_tableau(self):
        cards = [card for pile in self.tableau for card in pile]
        card_count = Counter((card.value, card.suit) for card in cards)

        expected_count = [
            (value, suit)
            for value in range(1, self.max_value + 1)
            for suit in ["H", "D", "S", "C"]
        ]
        errors = [card for card in expected_count if card_count[card] != 1]
        if errors:
            print("Tableau validation failed. Duplicate or missing cards:")
            print(errors)
            return False
        return True

    def valid_moves(self):
        """Generate all valid moves from the current state."""
        moves = []

        # Tableau to Foundation moves (high priority)
        for i, pile_from in enumerate(self.tableau):
            if not pile_from:
                continue
            card = pile_from[-1]
            if self.can_move_to_foundation(card):
                moves.append(("tableau_to_foundation", i))

        # Temp to Foundation moves (high priority)
        for card in sorted(self.temp_slots):
            if self.can_move_to_foundation(card):
                moves.append(("temp_to_foundation", card))

        # Tableau to Tableu move multiple cards at once if the cards being moved are in proper order,
        # and the top card being moved can be moved to the destination pile.
        # If temp has x empty spots, you can move x+1 cards at once.
        # If one of the piles other than the one we move from/to is empty, we can move (x+1)*2 cards.
        temp_allowed = self.max_temp_slots - len(self.temp_slots) + 1
        for i, pile_from in enumerate(self.tableau):
            if not pile_from or len(pile_from) == 1:
                continue
            for j in range(len(pile_from) - 1):
                this_range = pile_from[j:]
                if self.proper_order(this_range):
                    for k, pile_to in enumerate(self.tableau):
                        empty_piles_multiplier = 1 + sum(
                            1
                            for r in range(len(self.tableau))
                            if (r != i and r != k and self.tableau[r] == [])
                        )
                        if (
                            i != k
                            and self.can_place(this_range[0], pile_to)
                            and temp_allowed * empty_piles_multiplier >= len(this_range)
                        ):
                            moves.append(
                                (
                                    "tableau_to_tableau_multiple",
                                    i,
                                    k,
                                    len(pile_from) - j,
                                )
                            )

        # Tableau to Tableau moves
        for i, pile_from in enumerate(self.tableau):
            if not pile_from:
                continue
            card = pile_from[-1]
            for j, pile_to in enumerate(self.tableau):
                if i != j and self.can_place(card, pile_to):
                    moves.append(("tableau_to_tableau", i, j))

        # Temp to Tableau moves
        for card in sorted(self.temp_slots):
            for j, pile_to in enumerate(self.tableau):
                if self.can_place(card, pile_to):
                    moves.append(("temp_to_tableau", card, j))

        # Tableau to Temp moves
        if len(self.temp_slots) < self.max_temp_slots:
            for i, pile_from in enumerate(self.tableau):
                if not pile_from:
                    continue
                moves.append(("tableau_to_temp", i))

        return sorted(moves)

    def can_place(self, card, pile):
        """Check if the card can be placed on the given pile."""
        if not pile:
            return True  # Any card can be placed in an empty tableau spot
        top_card = pile[-1]
        return (card.color != top_card.color) and (card.value + 1 == top_card.value)

    def can_move_to_foundation(self, card):
        """Check if the card can be moved to its foundation."""
        return self.foundation[card.suit] + 1 == card.value

    def proper_order(self, cards):
        """Check if the cards are in proper order."""
        if not cards:
            return False
        if len(cards) == 1:
            return True
        return all(
            cards[i].value - 1 == cards[i + 1].value
            and cards[i].color != cards[i + 1].color
            for i in range(len(cards) - 1)
        )

    def apply_move(self, move):
        """Apply a move to the game state and return a new game state."""
        new_state = copy.deepcopy(self)
        if move[0] == "tableau_to_tableau":
            _, from_pile, to_pile = move
            card = new_state.tableau[from_pile].pop()
            new_state.tableau[to_pile].append(card)
        elif move[0] == "tableau_to_tableau_multiple":
            _, from_pile, to_pile, num_cards = move
            cards_to_move = new_state.tableau[from_pile][-num_cards:]
            new_state.tableau[from_pile] = new_state.tableau[from_pile][:-num_cards]
            new_state.tableau[to_pile].extend(cards_to_move)
        elif move[0] == "tableau_to_foundation":
            _, from_pile = move
            card = new_state.tableau[from_pile].pop()
            new_state.foundation[card.suit] = card.value
        elif move[0] == "tableau_to_temp":
            _, from_pile = move
            card = new_state.tableau[from_pile].pop()
            new_state.temp_slots.add(card)
        elif move[0] == "temp_to_tableau":
            _, card, to_pile = move
            new_state.temp_slots.remove(card)
            new_state.tableau[to_pile].append(card)
        elif move[0] == "temp_to_foundation":
            _, card = move
            new_state.temp_slots.remove(card)
            new_state.foundation[card.suit] = card.value
        return new_state

    def foundation_size(self):
        return sum(self.foundation.values())

    def auto_foundation_moves(self):
        # If the minimum value in foundation is x, then all cards with value x+1 and x+2 can be moved to foundation.
        min_value = min(self.foundation.values())
        moves = []
        for pile in self.tableau:
            if not pile:
                continue
            card = pile[-1]
            if (
                card.value == min_value + 1 or card.value == min_value + 2
            ) and self.can_move_to_foundation(card):
                moves.append(("tableau_to_foundation", self.tableau.index(pile)))
        for card in sorted(self.temp_slots):
            if (
                card.value == min_value + 1 or card.value == min_value + 2
            ) and self.can_move_to_foundation(card):
                moves.append(("temp_to_foundation", card))
        return sorted(moves)

    def apply_auto_foundation_moves(self):
        path = []
        auto_moves = self.auto_foundation_moves()
        while auto_moves:
            for auto_move in auto_moves:
                self = self.apply_move(auto_move)
                path.append(auto_move)
            auto_moves = self.auto_foundation_moves()
        return self, path

    def heuristic(self, power_factor=0):
        """Heuristic function: For each pile, compute a score for how well ordered it is.
        If it goes from large numbers to smaller numbers, it is a good case.
        If the number increases or stays the same, it is a bad case. Cost is how bad it is.
        Also, free slots and free columns are good, but subtracting them from the cost lead to longer search.
        """
        cost = 0
        for pile in self.tableau:
            for i in range(len(pile) - 1):
                card = pile[i]
                cost += sum(
                    1 for j in range(i + 1, len(pile)) if card.value < pile[j].value
                ) * pow(self.max_value - card.value, power_factor)

        # This formula is my earlier attempt. Much slower but still finds a solution.
        # cost = 0
        # for pile in self.tableau:
        #     for i in range(len(pile) - 1):
        #         card = pile[i]
        #         if card.value <= max([c.value for c in pile[i + 1 :]]):
        #             cost += max([c.value for c in pile[i + 1 :]]) + len(pile[i + 1 :])

        # These make sense but they don't really work.
        free_slots = self.max_temp_slots - len(
            self.temp_slots
        )  # Number of free temp slots
        free_columns = sum(
            1 for pile in self.tableau if len(pile) == 0
        )  # Free tableau columns
        return cost  # - (free_slots + free_columns)

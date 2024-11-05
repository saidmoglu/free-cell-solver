import time
import copy
import heapq
from itertools import count
from freecell_test_cases import test_cases
from Card import Card
from GameState import GameState


def generate_random_initial_state(max_value=13, num_piles=8, max_temp_slots=4):
    """Generate a random initial game state. May be unsolvable"""
    import random

    suits = ["H", "D", "S", "C"]
    tableau = [[] for _ in range(num_piles)]
    foundation = {suit: 0 for suit in suits}
    temp_slots = set()

    deck = [Card(value, suit) for value in range(1, max_value + 1) for suit in suits]
    random.shuffle(deck)

    for i, card in enumerate(deck):
        tableau[i % num_piles].append(card)

    return GameState(
        tableau, foundation, temp_slots, max_value, num_piles, max_temp_slots
    )


def a_star_search(initial_state, max_states=None):
    visited = set()
    priority_queue = []
    counter = count()  # A counter to ensure no direct comparison between states

    path = []
    initial_state, path_add = initial_state.apply_auto_foundation_moves()
    path.extend(path_add)
    heapq.heappush(
        priority_queue, (initial_state.heuristic(), next(counter), initial_state, path)
    )

    visited.add(hash(initial_state))

    while priority_queue:
        _, _, state, path = heapq.heappop(priority_queue)
        valid_moves = state.valid_moves()

        for move in valid_moves:
            new_state = state.apply_move(move)
            new_path = path + [move]
            new_state, path_add = new_state.apply_auto_foundation_moves()
            new_path.extend(path_add)
            if new_state.is_goal():
                print("Solution found!")
                print(f"Visited {len(visited)} states")
                print(f"Solution length: {len(new_path)}")
                print()
                return new_path, len(visited)
            state_hash = hash(new_state)
            if state_hash in visited:
                continue
            visited.add(state_hash)
            heapq.heappush(
                priority_queue,
                (
                    new_state.heuristic(),
                    next(counter),
                    new_state,
                    new_path,
                ),
            )

            if len(visited) % 10000 == 0:
                print(
                    f"Visited {len(visited)} states. Queue size: {len(priority_queue)}"
                )
                if len(visited) % 100000 == 0:
                    print(state.pretty_print())
        if max_states and len(visited) >= max_states:
            print("Max states reached.")
            break
    print("No solution found.")
    return None, None


def depth_a_star_search(initial_state, move_depth=1, max_states=None):
    """
    A* search extended to a fixed depth. We explore all states up to a certain depth, compute the heuristic for each state,
    and add them to the priority queue. We continue to explore the states with the lowest heuristic until we reach the goal.
    Depth set to 1 is equivalent to regular A* search above.
    """
    visited = set()
    priority_queue = []
    counter = count()  # A counter to ensure no direct comparison between states

    path = []
    initial_state, path_add = initial_state.apply_auto_foundation_moves()
    path.extend(path_add)
    heapq.heappush(
        priority_queue, (initial_state.heuristic(), next(counter), initial_state, path)
    )

    visited.add(hash(initial_state))

    while priority_queue:
        _, _, state, path = heapq.heappop(priority_queue)
        current_move_depth = 0
        next_explore_states = [(state, path)]
        while current_move_depth < move_depth:
            to_explore_states = copy.deepcopy(next_explore_states)
            next_explore_states = []
            for state, path in to_explore_states:
                valid_moves = state.valid_moves()
                for move in valid_moves:
                    new_state = state.apply_move(move)
                    new_path = path + [move]
                    new_state, path_add = new_state.apply_auto_foundation_moves()
                    new_path.extend(path_add)
                    if new_state.is_goal():
                        print("Solution found!")
                        print(f"Visited {len(visited)} states")
                        print(f"Solution length: {len(new_path)}")
                        print()
                        return new_path, len(visited)
                    state_hash = hash(new_state)
                    if state_hash in visited:
                        continue
                    visited.add(state_hash)
                    next_explore_states.append((new_state, new_path))
                    if len(visited) % 10000 == 0:
                        print(
                            f"Visited {len(visited)} states. Queue size: {len(priority_queue)}"
                        )
                        if len(visited) % 100000 == 0:
                            print(state.pretty_print())
            current_move_depth += 1
        for state, path in next_explore_states:
            heapq.heappush(
                priority_queue,
                (
                    state.heuristic(),
                    next(counter),
                    state,
                    path,
                ),
            )
        if max_states and len(visited) >= max_states:
            print("Max states reached.")
            break
    print("No solution found.")
    return None, None


# Run the cases from test_cases imported.
def run_test_cases(
    start_index=0,
    end_index=None,
    step_by_step_solution=False,
    max_states=1e6,
    move_depth=1,
):
    if end_index is None:
        end_index = len(test_cases)
    if end_index - start_index == 0:
        return
    start_time = time.time()
    solved_count = 0
    success_lengths = []
    visited_counts = []
    for test_case in test_cases[start_index:end_index]:
        initial_tableau = []
        suits = test_case.suits.strip().split("\n")
        values = [r.split() for r in test_case.values.strip().split("\n")]
        for i, row in enumerate(suits):
            initial_tableau.append(
                [Card(int(values[i][j]), row[j]) for j in range(len(row))]
            )

        initial_foundation = {
            "H": 0,
            "C": 0,
            "S": 0,
            "D": 0,
        }
        initial_temp_slots = set()

        initial_state = GameState(
            initial_tableau, initial_foundation, initial_temp_slots
        )

        assert initial_state.validate_tableau()
        print(initial_state.pretty_print())
        if step_by_step_solution:
            input("Press Enter to start solving...")
        # path, visited_count = a_star_search(initial_state, max_states)
        path, visited_count = depth_a_star_search(
            initial_state, move_depth=move_depth, max_states=max_states
        )
        if path:
            solved_count += 1
            visited_counts.append(visited_count)
            success_lengths.append(len(path))
        if step_by_step_solution:
            for move in path:
                initial_state = initial_state.apply_move(move)
                print(move)
                print(initial_state.pretty_print())
                input("Press Enter for next move...")
                print()
    print(f"Solved {solved_count}/{end_index-start_index} test cases.")
    print(f"Average solution length: {round(sum(success_lengths) / solved_count)}")
    print(f"Max solution length: {max(success_lengths)}")
    print(f"Average visited states: {round(sum(visited_counts) / solved_count)}")
    print(f"Max visited states: {max(visited_counts)}")
    print(f"visited_counts: {visited_counts}")
    print(f"Elapsed time: {time.time() - start_time:.2f} seconds")


# Test with random initial states. If there is a solution, print the test case.
def try_random_states(
    number_of_tests=4, max_states=1e6, print_test_case_state_threshold=0
):
    """
    Try to solve random initial states. Print the test case if a solution is found.
    number_of_tests: Number of random initial states to try.
    max_states: Maximum number of states to visit before giving up.
    print_test_case_state_threshold: Print the test case if the number of visited states is above this threshold.
    """
    if number_of_tests == 0:
        return
    failed_states = []
    successful_states = []
    success_lengths = []
    visited_counts = []
    for i in range(number_of_tests):
        initial_state = generate_random_initial_state()
        print(initial_state.pretty_print())
        solution, visited_count = a_star_search(initial_state, max_states)
        if solution:
            successful_states.append(initial_state)
            success_lengths.append(len(solution))
            visited_counts.append(visited_count)
        if not solution:
            failed_states.append(initial_state)
    print()
    print(
        f"Successful states with more than {print_test_case_state_threshold} visited states:"
    )
    for i, state in enumerate(successful_states):
        if visited_counts[i] > print_test_case_state_threshold:
            state.print_tableau_as_test_case()
    print()
    print(f"{len(failed_states)} failed states:")
    for state in failed_states:
        state.print_tableau_as_test_case()
    print()
    print(f"{len(successful_states)} successful states.")
    print(
        f"Average solution length: {round(sum(success_lengths) / len(success_lengths))}"
    )
    print(f"Max solution length: {max(success_lengths)}")
    print(f"Average visited states: {round(sum(visited_counts) / len(visited_counts))}")
    print(f"Max visited states: {max(visited_counts)}")
    print(f"visited_counts: {visited_counts}")
    print()
    print(f"{len(failed_states)} failed states.")


run_test_cases(start_index=0, end_index=1, step_by_step_solution=True, max_states=3e5)
try_random_states(
    number_of_tests=0, max_states=1e6, print_test_case_state_threshold=1e4
)

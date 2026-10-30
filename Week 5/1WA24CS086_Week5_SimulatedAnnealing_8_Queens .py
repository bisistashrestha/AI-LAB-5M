print("Name: Bisista Shrestha\nUSN: 1WA24CS086")
import random
import math


def calculate_cost(state):
    """
    Count pairs of queens attacking each other.
    state[i] represents the row of the queen in column i.
    """
    conflicts = 0
    n = len(state)

    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j]:
                conflicts += 1
            elif abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1

    return conflicts


def get_random_successor(state):
    """
    Generate a successor by moving one queen
    to a random row in its column.
    """
    successor = state.copy()
    column = random.randrange(len(state))

    new_row = random.randrange(len(state) - 1)
    if new_row >= successor[column]:
        new_row += 1

    successor[column] = new_row
    return successor


def schedule(t):
    """Temperature decreases over time."""
    return max(0.01, 10 * (0.99 ** t))


def simulated_annealing():
    n = 8

    # Initial state: one queen in each column
    current = [random.randrange(n) for _ in range(n)]

    print("Initial state:", current)
    print("Initial cost:", calculate_cost(current))

    t = 0

    while True:
        temperature = schedule(t)

        # Stop when temperature is effectively zero
        if temperature < 0.02:
            break

        next_state = get_random_successor(current)

        # Cost is the number of attacking pairs.
        # Lower cost means a better state.
        delta_e = (
            calculate_cost(current) -
            calculate_cost(next_state)
        )

        if delta_e > 0:
            # Better state: always accept
            current = next_state
        else:
            # Worse or equal state: accept probabilistically
            probability = math.exp(delta_e / temperature)

            if random.random() < probability:
                current = next_state

        t += 1

        if calculate_cost(current) == 0:
            print("\nSolution found!")
            print("Final state:", current)
            print("Final cost:", calculate_cost(current))
            print("Iterations:", t)
            return current

    print("\nTemperature reached the stopping limit.")
    print("Final state:", current)
    print("Final cost:", calculate_cost(current))

    return current


solution = simulated_annealing()

print("Name: Bisista Shrestha\nUSN:1WA24CS086")
def cost(state):
    conflicts = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            if (state[i] == state[j] or
                    abs(state[i] - state[j]) == abs(i - j)):
                conflicts += 1
    return conflicts

def get_neighbors(state):
    neighbors = []
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            neighbor = state.copy()
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append((neighbor, (i, j), cost(neighbor)))

    return neighbors

def hill_climbing(initial_state):
    state = initial_state.copy()
    step = 1

    while True:
        print(f"\nStep {step}")
        print(f"Neighbours of {state} (cost is {cost(state)})")

        neighbors = get_neighbors(state)
        for neighbor, pair, neighbor_cost in neighbors:
            print(
                f"x0 = {neighbor[0]}, x1 = {neighbor[1]}, "
                f"x2 = {neighbor[2]}, x3 = {neighbor[3]} "
                f"(cost is {neighbor_cost})"
            )
        best_neighbor, best_pair, best_cost = min(
            neighbors, key=lambda item: item[2]
        )
        if best_cost >= cost(state):
            print("\nNo better neighbor. Algorithm terminates.")
            break

        print(
            f"\nChoose this neighbor: {best_neighbor} "
            f"(swap x{best_pair[0]} and x{best_pair[1]})"
        )

        state = best_neighbor
        step += 1

        if best_cost == 0:
            print("\nGoal state reached!")
            print(f"Final state: {state}")
            break


initial_state = [3, 1, 2, 0]
hill_climbing(initial_state)

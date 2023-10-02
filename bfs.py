def water_jugs_bfs(goal_state):
    capacity1 = 3
    capacity2 = 1
    visited = []
    queue = [(0, 0)]                                # The initial state is (0, 0)
    paths = [[queue[0]]]

    while len(queue) > 0:
        print("------------------------------")
        print(queue)
        state = queue.pop(0)
        visited.append(state)
        current_path = paths.pop(0)

        # Check if the current state is the goal state
        if state == goal_state:
            print("------------------------------")
            print("Using Breadth First Search to Solve:", goal_state[:])
            print("Path :",current_path)
            print("Nodes expanded: ", visited)
            return None

        # Generate the next states.
        if state[0] < capacity1:                    # Fill Jug A
            next_state = (capacity1, state[1])
            if next_state not in visited:
                queue.append(next_state)
                paths.append(current_path + [next_state])
        if state[1] < capacity2:                    # Fill Jug B
            next_state = (state[0], capacity2)
            if next_state not in visited:
                queue.append(next_state)
                paths.append(current_path + [next_state])
        if state[0] > 0 and state[1]<capacity2:     # pour from Jug A into B
            amount = min(state[0], capacity2 - state[1])
            next_state = (state[0] - amount, state[1] + amount)
            if next_state not in visited:
                queue.append(next_state)
                paths.append(current_path + [next_state])
        if state[1] > 0  and state[0]<capacity1:    # pour from Jug B into A
            amount = min(state[1], capacity1 - state[0])
            next_state = (state[0] + amount, state[1] - amount)
            if next_state not in visited:
                queue.append(next_state)
                paths.append(current_path + [next_state])
        if state[0] > 0:                            # Empty Jug A
            next_state  = (0,state[1])
            if next_state not in visited:
                queue.append(next_state)
                paths.append(current_path + [next_state])
        if state[1] > 0:                            # Empty Jug B
            next_state = (state[0],0)
            if next_state not in visited:
                queue.append(next_state)
                paths.append(current_path + [next_state])

    return None

# Example usage:
#goal_state = (2, 0)
#water_jugs_bfs(goal_state)
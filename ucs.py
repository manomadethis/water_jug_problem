import queue

def water_jugs_ucs(goal_state):
    capacity1 = 3
    capacity2 = 1
    visited = set()
    queue = [[0, (0, 0)]]                                                   # Initialize the weight and state of the queue
    paths = [[queue[0]]]

    while len(queue) > 0:
        print("------------------------------")
        print(queue)
        state = queue.pop(0)
        cur_path = paths.pop(0)

        # Only consider the state, not the weight
        current_state = state[1]

        if current_state == goal_state:
            cur_path = sorted(cur_path)
            print("------------------------------")
            print("Using Uniform Cost Search to Solve:", goal_state[:])
            print("Path:", cur_path)
            print("Nodes expanded:", visited)
            return None

        # Check if the state has been visited
        if current_state not in visited:
            visited.add(current_state)

            # Generate the states
            if current_state[0] < capacity1:    # Fill Jug A and allocate the appropriate weight
                weights = state[0] + 2
                next_state = [weights, (capacity1, current_state[1])]
                queue.append(next_state)
                paths.append(cur_path + [next_state])

            if current_state[1] < capacity2:    # Fill Jug B and allocate the appropriate weight
                weights = state[0] + 1
                next_state = [weights, (current_state[0], capacity2)]
                queue.append(next_state)
                paths.append(cur_path + [next_state])

            if current_state[0] > 0 and current_state[1] < capacity2:   # Pour Jug A into Jug B
                weights = state[0] + 3
                amount = min(current_state[0], capacity2 - current_state[1])
                next_state = [weights, (current_state[0] - amount, current_state[1] + amount)]
                queue.append(next_state)
                paths.append(cur_path + [next_state])

            if current_state[1] > 0 and current_state[0] < capacity1:   # Pour Jug B into Jug A
                weights = state[0] + 4
                amount = min(current_state[1], capacity1 - current_state[0])
                next_state = [weights, (current_state[0] + amount, current_state[1] - amount)]
                queue.append(next_state)
                paths.append(cur_path + [next_state])

            if current_state[0] > 0:    # Empty Jug A
                weights = state[0] + 6
                next_state = [weights, (0, current_state[1])]
                queue.append(next_state)
                paths.append(cur_path + [next_state])

            if current_state[1] > 0:    # Empty Jug B
                weights = state[0] + 5
                next_state = [weights, (current_state[0], 0)]
                queue.append(next_state)
                paths.append(cur_path + [next_state])

    return None

# Example usage:
#goal_state = (2, 0)
#water_jugs_ucs(goal_state)
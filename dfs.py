import queue

def water_jugs_dfs(goal_state):
    capacity1 = 3
    capacity2 = 1
    visited = []
    stack = [(0,0)] #initialize the stack to the starting state
    paths =[[stack[-1]]]

    while len(stack) != 0:
        print("------------------------------")
        print(stack)
        state = stack.pop(-1)
        visited.append(state)
        cur_path =paths.pop(-1)

        # Checks to see if the goal state has been achieved
        if state == goal_state:
            print("------------------------------")
            print("Using Depth First Search to Solve:", goal_state[:])
            print("Path:",cur_path)
            print("Nodes visited:", visited)
            return None

        # Generates the next states.
        if state[0] < capacity1:         #Fill jug A
            next_state = (capacity1,state[1])
            if next_state not in visited:
                stack.append(next_state)
                paths.append(cur_path + [next_state])

        if state[1] < capacity2:    # Fill jug B
            next_state =(state[0],capacity2)
            if next_state not in visited:
                stack.append(next_state)
                paths.append(cur_path+[next_state])

        if state[0] >0 and state[1] < capacity2: # Pour from jug A into jug B
            amount=min(state[0],capacity2 -state[1])
            next_state=(state[0] - amount, state[1] + amount)
            if next_state not in visited:
                stack.append(next_state)
                paths.append(cur_path+[next_state])

        if state[1] > 0 and state[0] <capacity1: # Pour from jug A into jug B
            amount = min(capacity1 -  state[0],state[1])
            next_state =(state[0] + amount, state[1] - amount)
            if next_state not in visited:
                stack.append(next_state)
                paths.append(cur_path+[next_state])

        if state[0] > 0: #Empty Jug A
            next_state =(0,state[1])
            if next_state not in visited:
                stack.append(next_state)
                paths.append(cur_path+[next_state])

        if state[1] >0: # Empty Jug B
            next_state =(state[0],0)
            if next_state not in visited:
                stack.append(next_state)
                paths.append(cur_path + [next_state])

    return None

# Example usage:
#goal_state = (2, 0)
#water_jugs_dfs(goal_state)

from collections import deque

def is_valid_state(missionaries_left, cannibals_left, missionaries_right, cannibals_right):
    if missionaries_left < 0 or cannibals_left < 0 or missionaries_right < 0 or cannibals_right < 0:
        return False
    if missionaries_left > 0 and missionaries_left < cannibals_left:
        return False
    if missionaries_right > 0 and missionaries_right < cannibals_right:
        return False
    return True

def is_goal_state(state):
    return state == (0, 0, 3, 3, 0)

def missionaries_and_cannibals():
    initial_state = (3, 3, 0, 0, 1)
    queue = deque([(initial_state, [])])
    visited = set()
    visited.add(initial_state)

    while queue:
        state, path = queue.popleft()
        missionaries_left, cannibals_left, missionaries_right, cannibals_right, boat = state

        if is_goal_state(state):
            return path + [state]

        moves = []
        if boat == 1:
            moves = [(1, 0), (0, 1), (1, 1), (2, 0), (0, 2)]
        else:
            moves = [(-1, 0), (0, -1), (-1, -1), (-2, 0), (0, -2)]

        for m, c in moves:
            if boat == 1:
                new_state = (missionaries_left - m, cannibals_left - c, missionaries_right + m, cannibals_right + c, 0)
            else:
                new_state = (missionaries_left + m, cannibals_left + c, missionaries_right - m, cannibals_right - c, 1)

            if is_valid_state(new_state[0], new_state[1], new_state[2], new_state[3]) and new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [state]))

    return None

solution = missionaries_and_cannibals()

if solution:
    for step in solution:
        print(step)
else:
    print("No solution found.")


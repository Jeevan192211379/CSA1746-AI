from collections import deque


def can_measure_water(m, n, d):
    if d > max(m, n) or d % gcd(m, n) != 0:
        return False
    return True


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def water_jug_problem(m, n, d):
    if not can_measure_water(m, n, d):
        print("No solution exists")
        return

    visited = set()
    queue = deque()

    queue.append((0, 0, []))  

    while queue:
        a, b, path = queue.popleft()

        if a == d or b == d:
            path.append((a, b))
            print(f"Solution found: {path}")
            return

        if (a, b) in visited:
            continue
        visited.add((a, b))

        actions = [
            (m, b, path + [(a, b)]),  
            (a, n, path + [(a, b)]),  
            (0, b, path + [(a, b)]),  
            (a, 0, path + [(a, b)]),  
            (min(a + b, m), max(0, a + b - m), path + [(a, b)]),  
            (max(0, a + b - n), min(a + b, n), path + [(a, b)]) 
        ]

        for action in actions:
            if (action[0], action[1]) not in visited:
                queue.append(action)

    print("No solution found")


m = 4  
n = 3  
d = 2  

water_jug_problem(m, n, d)

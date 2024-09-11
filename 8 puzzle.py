import heapq


class PuzzleState:
    def __init__(self, board, move_count=0, previous=None):
        self.board = board
        self.move_count = move_count
        self.previous = previous
        self.empty_pos = self.find_empty()


    def find_empty(self):
        for i, row in enumerate(self.board):
            if 0 in row:
                return i, row.index(0)


    def manhattan_distance(self):
        distance = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != 0:
                    correct_pos = divmod(self.board[i][j] - 1, 3)
                    distance += abs(correct_pos[0] - i) + abs(correct_pos[1] - j)
        return distance


    def generate_moves(self):
        moves = []
        x, y = self.empty_pos
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_board = [row[:] for row in self.board]
                new_board[x][y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[x][y]
                moves.append(PuzzleState(new_board, self.move_count + 1, self))

        return moves


    def is_goal(self):
        goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        return self.board == goal


    def __lt__(self, other):
        return (self.manhattan_distance() + self.move_count) < (other.manhattan_distance() + other.move_count)


def solve_puzzle(start_board):
    start_state = PuzzleState(start_board)
    open_list = []
    closed_set = set()
    heapq.heappush(open_list, start_state)

    while open_list:
        current_state = heapq.heappop(open_list)

        if current_state.is_goal():
            return reconstruct_path(current_state)

        closed_set.add(tuple(tuple(row) for row in current_state.board))

        for move in current_state.generate_moves():
            if tuple(tuple(row) for row in move.board) not in closed_set:
                heapq.heappush(open_list, move)

    return None


def reconstruct_path(state):
    path = []
    while state:
        path.append(state.board)
        state = state.previous
    return path[::-1]


start_board = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

solution = solve_puzzle(start_board)

if solution:
    print("Solution found in {} moves:".format(len(solution) - 1))
    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("No solution found.")

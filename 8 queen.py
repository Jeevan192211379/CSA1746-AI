
def print_board(board):
    for row in board:
        print(" ".join(str(x) for x in row))
    print()


def is_safe(board, row, col, n):

    for i in range(col):
        if board[row][i] == 1:
            return False


    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False


    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens(board, col, n):
    
    if col >= n:
        return True

    
    for i in range(n):
        if is_safe(board, i, col, n):
            
            board[i][col] = 1

            
            if solve_n_queens(board, col + 1, n):
                return True

        
            
            board[i][col] = 0

    return False


def solve():
    n = 8
    board = [[0 for _ in range(n)] for _ in range(n)]

    if not solve_n_queens(board, 0, n):
        print("Solution does not exist")
        return False

    print("Solution for the 8-Queen problem:")
    print_board(board)
    return True


solve()

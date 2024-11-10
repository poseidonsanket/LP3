def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def util(board, col):
    if col >= N:
        return True

    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1
            if util(board, col + 1):
                return True
            board[i][col] = 0

    return False

# Take user input for board size
N = int(input("Enter the size of the board (e.g., 8 for 8x8): "))

# Initialize the board
board = [[0 for i in range(N)] for i in range(N)]

# Solve the N-Queens problem and print the solution
if util(board, 0) == False:
    print("Solution does not exist")
else:
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print("-", end=" ")
        print()

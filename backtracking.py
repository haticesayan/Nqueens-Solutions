def backtracking(board, column, n):
    # Use backtracking to find all solutions
    # start from leftmost column
    if column >= n:
        return True             # if all queens are placed simply return
    for i in range(n):      # Try all the rows in the current column
        if safe(board, i, column, n):  # Check if queen can be placed here safely
            board[i][column] = "Q"  # if yes mark the queen with "Q" mark
            if backtracking(board, column + 1, n) : # solve the rest of the problem recursively
                return True
            board[i][column] = "X"
    return False


def safe(board, row, column, n):
    # Check if it's safe to place a queen at board[x][y]
    # check row on left side
    # if there is a queen in the same column it is not safe
    for j in range(column):
        if board[row][j] == "Q":
            return False

    # check upper diagonal
    # if there is a queen in the same upper diagonal it is not safe
    i, j = row, column
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":  # if there is a queen in the same upper diagonal it is not safe
            return False
        i = i - 1
        j = j - 1

    # check lower diagonal

    x, y = row, column
    while x < n and y >= 0:
        if board[x][y] == "Q":  # if there is a queen in the same lower diagonal it is not safe
            return False
        x = x + 1
        y = y - 1

    return True  # else it is safe

# print the board
def print_board(board):
     for row in board:
        print(" ".join(row))

def queen_input():
    # takes number of queens
            n = int(input('Enter the number of queens '))
            if n <= 3:
                print("Value should be greater than or equal to 4")
            return n
while True:

    # Takes number of queens as input
  n = queen_input()

  # create a n by n board
  board = ["X"] * n
  for i in range(n):
     board[i] = ["X"] * n

  # Solving with backtracking
  if not backtracking(board, 0, n):
      print("No solution exists")
  else:
   print("One of the solutions is: \n")
   print_board(board);

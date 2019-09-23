from tabulate import tabulate

row = ["o"]*4
board = [row]*4
board[1][1] = "x"

print(tabulate(board))

def print_board(board):
    for i, row in enumerate(board):
        row_str = " "
        for j, value in enumerate(row):
            row_str += value
            if j != len(row) - 1:
                row_str += "  | "
        print(row_str)
        if i != len(board) - 1:
            print("---------------")


def get_move(turn, board):
    while True:
        row = int(input("row: "))
        col = int(input("col: "))

        if row < 1 or row > len(board):
            print("invalid row, try again ")
        elif col < 1 or col > len(board[row - 1]):
            print("invalid col, try again ")
        elif board[row - 1][col - 1] != " ":
            print("already taken, try again")
        else:
            board[row - 1][col - 1] = turn
            break


# tuple is immutable, works like a list but its values cannot be changed
def check_win(board, turn):
    lines = [[(0,0 ), (0,1), (0,2)],
             [(1,0),(1,1),(1,2)],
             [(2,0),(2,1),(2,2)],
             [(0,0),(1,0),(2,0)],
             [(0,1),(1,1),(2,1)],
             [(0,2),(1,2),(2,2)],
             [(0,0),(1,1),(2,2)],
             [(0,2),(1,1),(2,0)]
             ]
    for line in lines:
        win = True
        for pos in line:
            row, col = pos
            if board[row][col] != turn:
                win = False
                break
        if win:
            return True
        
    return False

board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

turn = "X"
turn_number = 0

print_board(board)
while turn_number < 9:
    print()
    print("it is the ", turn, "player turn. please make your move ")
    get_move(turn, board)
    print_board(board)
    winner = check_win(board, turn)
    if winner:
        break
    if turn == "X":
        turn = "O"
    else:
        turn = "X"
    turn_number += 1

if turn_number == 9:
    print("tied game")
else:
    print("the winner was, ", turn)
# Week 6 day 3
# Activity-Any-Column.pdf
# Steven Daniel

def did_I_win_down(player, board):
    all_win = False
    for x in range(3):          # for each column
        did_win = True          # dit win column?
        for i in range(3):      # for each row
            did_win &= player == board[i][x]
        all_win |= did_win
    return all_win

def print_2D_board(b):
    for i in range(len(b)):
        print(b[i])

def main():
    boards = [[["X", "O", "O"] ] * 3, \
             [["X", "O", "X"], ["O"] * 3, ["O", "X", "O"]], \
             [["O", "O", "X"], ["O", "X", "O"], ["X", "O", "O"]], \
             [["O", "O", "X"]] * 3]
    for b in boards:
        print_2D_board(b)
        print("X won?",  did_I_win_down("X", b))
        print("O won?", did_I_win_down("O", b))

if __name__ == "__main__":
    main()
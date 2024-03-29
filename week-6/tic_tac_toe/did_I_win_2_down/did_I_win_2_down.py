# Week 6 day 3
# Activity-One-Column.pdf
# Steven Daniel

def did_I_win_2_down(player, board):
    did_win = True
    for i in range(3):
        did_win &= player == board[i][2]
    return did_win
  
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
        print("X won?",  did_I_win_2_down("X", b))
        print("O won?", did_I_win_2_down("O", b))

if __name__ == "__main__":
    main()
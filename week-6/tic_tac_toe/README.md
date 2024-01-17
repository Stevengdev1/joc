Arrays & Dictionaries

Activity:Problem Solving

did_I_win_2_down(player, board) Write a function did_I_win_2_down that takes a player string and a two-dimensional 3 x 3 tic-tac-toe board as parameters and returns whether the player won with a column to the right.

Example function call(s):                                   Returns:
did_I_win_2_down(“X", [['O', 'O', 'X'],\['o', 'x', 'O'], \  False['X', 'O', 'O']]
did_I_win_2_down("O", [['O', 'O', 'X'],\['o', 'X', 'O'], \  False['X','O', 'O']]
did_I_win_2_down(“X", [['O', 'O', 'X'], \['o', 'o', 'X'], \ True['O', 'O', 'X']]
did_I_win_2_down("O", [['O', 'O', 'X'], \['o', 'o', 'x'], \ False['o', 'o', 'X']]

Possible Solutions?

def did_I_win_2_down(player, board):
# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14OEKew3GY7qL3r4-NA0NTpSGky6KVIik
"""

# define the board
board = [["_" for i in range(3)] for j in range(3)]

# define the player's move
def make_move(board, player, row, col):
  board[row][col] = player

# define the function to check for a winner
def check_winner(board):
  # check rows
  for row in range(3):
    if board[row][0] == board[row][1] and board[row][1] == board[row][2] and board[row][0] != "_":
      return board[row][0]

  # check columns
  for col in range(3):
    if board[0][col] == board[1][col] and board[1][col] == board[2][col] and board[0][col] != "_":
      return board[0][col]

  # check diagonals
  if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != "_":
    return board[0][0]
  if board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[2][0] != "_":
    return board[2][0]

  # if there is no winner, return None
  return None

# define the function to check if the game is a draw
def check_draw(board):
  for row in range(3):
    for col in range(3):
      if board[row][col] == "_":
        return False
  return True

# define the function to play the game
def play_game():
  # Use constants for player symbols in case we want to use different symbols in the future.
  PLAYER_X = "X"
  PLAYER_O = "O"
  # initialize the game
  player = PLAYER_X
  winner = None
  draw = False

  # loop until the game is over
  while not winner and not draw:
    # print the current board
    for row in board:
      print(" ".join(row))

    
    # get the player's move
    # Improvement1: check if the input is valid
    try:
      row = int(input("Enter row (0-2): "))
      col = int(input("Enter column (0-2): "))
    except ValueError:
      print("Invalid input. Please enter an integer value between 0 and 2.")
      continue

    
    if row < 0 or row > 2 or col < 0 or col > 2:
      print("Invalid input. Please enter a value between 0 and 2.")
      continue

    # improvement2: check if the cell is already occupied
    if board[row][col] != "_":
      print("That cell is already occupied. Please choose a different cell.")
      continue

    make_move(board, player, row, col)
    
    

    # check for a winner
    winner = check_winner(board)

    # check for a draw
    draw = check_draw(board)

    # switch players
    if player == PLAYER_X:
      player = PLAYER_O
    else:
      player = PLAYER_X

  # print the final board
  for row in board:
    print(" ".join(row))

  # print the result of the game
  if winner:
    print(f"Player {winner} wins!")
  else:
    print("The game is a draw.")

# play the game
play_game()
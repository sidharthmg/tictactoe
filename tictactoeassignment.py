import os
import time
from random import randint
from IPython.display import clear_output

board=["-"]*10

def display_board(board):
     clear_output()
     print(board[0]+'|'+ board[1]+ '|'+board[2])
     print(board[3]+'|'+ board[4]+'|' + board[5)
     print(board[6]+'|'+ board[7]+'|' + board[8])

def computer_ch():
    computer_pos=random.randint(0,8)

def player_input():
     print("\n Welcome to tic tac toe.This game takes place between the player and computer.")
     marker=()
     while(marker!='X' and marker!='O'):
          marker=input("Choose X or O:")
     player=marker
          if player='X':
             computer='O'
          else
              computer='X'
          return(player,computer)
     print("\n Computer has chosen",computer)

def first_move():
     first=random.randint(0,1)
       if first==0:
          return "Player"
       else
            return "Computer"


def play_game():
     game_still_going = True
     display_board()
     while game_still_going:
          handle_turn()
          check_if_game_over()
     if winner == player
          print("Player won")
     elif winner==computer
          print ("Computer won")
     elif winner == None:
          print("Tie.")

def handle_turn(choice)
     firstchoice=first_move()
     print("/n The first move goes to",firstchoice)
       if firstchoice== "Player":
          position = int(input("Choose a position from 1-9: "))
          valid = True
          while valid:
               while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    position = input("Choose a position from 1-9: ")
               position = int(position) - 1
               if board[position] == "-":
                    valid = False
               else:
                    print("You can't go there. Go again.")

          board[position] = player
          display_board()
       else
            position=computer_ch()-1
            valid=True
            while valid:
              if board[position]=="-":
                 valid=False
              else
                 position=computer_ch()-1
                 continue
            board[position]=computer
            display_board()

def check_if_game_over():
  check_for_winner()
  check_for_tie()

def check_for_winner():
  winner=""
  row_winner = check_rows()
  column_winner = check_columns()
  diagonal_winner = check_diagonals()
  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None

def check_rows():
  game_still_going=True
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  if row_1 or row_2 or row_3:
    game_still_going = False
  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]
  else:
    return None

def check_columns():
  game_still_going=True
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"
  if column_1 or column_2 or column_3:
    game_still_going = False
  if column_1:
    return board[0]
  elif column_2:
    return board[1]
  elif column_3:
    return board[2]
  else:
    return None

def check_diagonals():
  game_still_going=True
  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[2] == board[4] == board[6] != "-"
  if diagonal_1 or diagonal_2:
    game_still_going = False
  if diagonal_1:
    return board[0]
  elif diagonal_2:
    return board[2]
  else:
    return None

def check_for_tie():
  game_still_going=True
  if "-" not in board:
    game_still_going = False
  else:
     pass










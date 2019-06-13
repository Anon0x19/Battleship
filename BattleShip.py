from random import randint  #imports the randint (random integer) from the random module

board = []

for x in range(0, 5):
  board.append(["O"] * 5)   #it appends "0" 5 times to board and repeats it 5 times

def print_board(board):   #defines the print_board function with the specific "board" parameter
  for row in board:
    print " ".join(row)   #it prints the 5 "0" in 5 different rows

print_board(board)  #runs the print_board function while using the board as parameter

def random_row(board):
  return randint(0, len(board) - 1)   #chooses a ranom row between 0 and the maximum value in the board and subtracts 1 and the first value in the list is 0 and randint wont choose 0

def random_col(board):
  return randint(0, len(board[0]) - 1)  #chooses a ranom column between 0 and the maximum value in the board and subtracts 1 and the first value in the list is 0 and randint wont choose 0

ship_row = random_row(board) #creates the variable ship_row and sets it to the random row
ship_col = random_col(board) #creates a variable called ship_col and sets it to the ranom column

for turn in range(4):
  print "Turn", turn + 1    #repeats the code for all integers between 0 and 4, and adds a 1 to the turn
  guess_row = int(raw_input("Guess Row: "))   #asks the user to input a row
  guess_col = int(raw_input("Guess Col: "))   #asks the user to input a column

  if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sank my battleship!"    #if you guess correctly both row and column, you "sink" the battle ship and complete the aim of the game
    break
  else:
    if guess_row not in range(5) or \
      guess_col not in range(5):
      print "Oops, that's not even in the ocean."   #checks if the input is greater than 5 and if it is it prints the error message
    elif board[guess_row][guess_col] == "X":
      print( "You guessed that one already." )    #checks if the specific location has been replaced with an X and if it has, it returns the "error" message saying you have guessed that location already
    else:
      print "You missed my battleship!"
      board[guess_row][guess_col] = "X"     #replaces the 0 in the location you have specified with an X
    if (turn == 3):
      print "Game Over"   #if turns is exactly 3, it prints the message "Game Over"
    print_board(board)

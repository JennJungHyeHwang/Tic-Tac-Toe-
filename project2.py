'''Project 2

Jenn Hwang
I certify that this work was done in accordance with
GV academic honesty policies.

fall, 2022'''

#This function prints the list as a 3x3 grid
def printBoard(b):
    count = 0
    print("--------------" )
    for i in b:
        if count == 0 or count == 3 or count == 6:
          print( "| " + i + " ", end='|')
        else:
          print( i + " ", end='|')
        count = count + 1
        if count % 3 == 0:
            print( "\n" + "--------------" )

#this function takes parameters the words list, the used list, and a word.
#If the chosen word is not in the words list, it is false. Otherwise, it is true
def chooseWord(words, used, word):
    if word not in words:
        return False
    else:
        used.add(word)
        return True
#This function does checks on rows
def checkRows(board):
  for i in range(9):
    # if the second letter in a row have the same char, then return true
    # board [word] [1=second letter]
    if board[i] != "" and board[i + 1] != "" and board[i + 2] != "":
      if (board[i][1] == board[i + 1][1] == board[i + 2][1]):
        return True
      # else +3 to increase the row
      else:
        i += 3
    # when no rows are found, return false
  return False

#This function does checks on columns
def checkCols(board):
    for i in range(9):
    #board[the position on the board][2ndletter]
      if board[i] != "" and board[i+3] != "" and board[i+6] != "":
        if (board[i][1] == board[i+3][1] == board[i+6][1]):
            return True
        #else +1 to increase to next column
        else:
            i += 1
    return False
#This function does a left diagonal check
def checkLeftDiag(board):
    if board[0] != "" and board[4] != "" and board[8] != "":
      if (board[0][1] == board[4][1] == board[8][1]):
          return True
      else:
          return False
#This function does a right diagonal check
def checkRightDiag(board):
    if board[2] != "" and board[4] != "" and board[6] != "":
      if (board[2][1] == board[4][1] == board[6][1]):
          return True
      else:
          return False

#The main function
def main():
    board = ['' for i in range(0,9)] #A list with 9 empty strings inside
    words = set(["hen", "bee", "less", "air", "bits", "lip", "soda", "book", "lot"]) #Allthe starter words'
    used = set()  #A list that begins empty
    gameOver = False #To determine when to end the game
    player = 1


    while gameOver != True: #Loop until gameOver is True
        print("This is the board:")
        printBoard(board)
        # print(board)
        print("These are the available words to pick from:")
        print(words)
        print("The player to choose the word is", player)
        word = input("Enter a word from the word list")
        while not chooseWord(words, used, word):
            print("Enter a word from the word list")
            word = input()

    #Once a valid word is chosen, ask the user which position they wish to add it to on
#the board. The positions should be 0-8 and correspond to these positions:
        position = int(input("Which position would you like to add the word to?: (0-8)"))
        while position not in range(0, 9) or board[position] != "":
            position = int(input("Choose a valid position to add: (0-8)"))
        board[position] = word
        words.remove(word)
#Each of the win condition checks
        if checkRows(board) or checkCols(board) or checkLeftDiag(board) or checkRightDiag(board) is True:
            words = []
        if len(words) == 0:
            gameOver = True
            printBoard(board)
            print(f'Player {player} Wins!')
            print('\nGame Over!')
        if player == 1: #Players take turns
           player = 2
        elif player == 2:
           player = 1
main()
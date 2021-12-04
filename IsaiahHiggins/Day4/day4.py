import sys
import os
sys.path.insert(1, 'C:/Users/Isaiah Higgins/Documents/GitHub/2021AdventOfCode/IsaiahHiggins')
import Common as com

sample = os.path.realpath('sample.txt')
real = os.path.realpath('Real.txt')

content = com.readAndCleanLine(real)
#content = com.readAndCleanLine(sample)
answer =0   

def checkBoard(board):
    for row in board:
        if row.count('x') == len(row):
            return True
    columns = com.getCol(board)
    for col in columns:
        if col.count('x') == len(col):
            return True
    return False



# file content
draws = content[0].split(',')

# parse
board = []
boardIndex = 0
every_board = list()
for i in range(1, len(content)):
    if content[i] != '':
        board.append(content[i].split())
    else:
        every_board.append(board)
        board = []
every_board.append(board)

every_board = every_board[1:]


solutionFound = False
winningBoards = []
winningDraw = -1
losingBoard= -1
# make moves and check for win
for draw in draws:
    #boards
    if not solutionFound:
        for currentBoard in range(0, len(every_board)):
            # get every row
            for row in range(0, len(every_board[currentBoard])):
                # go over every entry in a row
                for entry in range(0, len(every_board[currentBoard][row])):
                    if every_board[currentBoard][row][entry] == draw:
                        every_board[currentBoard][row][entry] = 'x'
            if(checkBoard(every_board[currentBoard])):
                if not(currentBoard in winningBoards):
                    winningBoards += [currentBoard]
                    winningDraw = draw
                    if len(winningBoards) == len(every_board):
                        losingBoard = currentBoard
                        solutionFound = True
                
    else:
        break

# get answer
for row in every_board[losingBoard]:
    for char in row:
        if char.isnumeric():
            answer += int(char)
print(winningDraw)
print(answer * int(winningDraw))














from enum import unique
from xml.dom import minidom
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
import os
import argparse

if __name__ == '__main__':
    p = argparse.ArgumentParser(description='...')
    p.add_argument('--puzzle_name', required=False)
    p.add_argument('-solve_on_startup', default=False)
    p.add_argument('-time_delay', default=0)
    p.add_argument('-solution_name', default=0)
    p.add_argument('-exit_on_solve', default=False)
    args = p.parse_args()

# Hides root window for now
# >>> File Selector <<<
#Tk().withdraw() 
    # show an "Open" dialog box and return the path to the selected file
#file = askopenfilename()

file = args.puzzle_name
if os.path.isfile(file): 
   file = minidom.parse(file)

name = file.getElementsByTagName('name')[0]
sRowsPerBox = file.getElementsByTagName('rows_per_box')[0]
sColsPerBox = file.getElementsByTagName('cols_per_box')[0]
startState = file.getElementsByTagName('start_state')[0]
wellFormed = file.getElementsByTagName('well_formed')[0]
solvable = file.getElementsByTagName('solvable')[0]

uniqueSolution = file.getElementsByTagName('unique_solution')[0]
pigeonholeDecidable = file.getElementsByTagName('pigeonhole_decidable')[0]

try:    
    startState = eval(startState.firstChild.data.replace("\\","").replace("\n","").replace("\t",""))
except: startState = 'none'
rowsPerBox = int(sRowsPerBox.firstChild.data)
colsPerBox = int(sColsPerBox.firstChild.data)
solvable = bool(solvable.firstChild.data)


board = []
row = []
gridline = []
for col in range(0,colsPerBox*rowsPerBox):
    gridline.append(0)
grid = []
for row in range(0,colsPerBox*rowsPerBox):
    board.append(list(gridline))

# Populate board with inital starting state
if rowsPerBox !=0 and colsPerBox !=0 and solvable == True and startState != 'none':
    for row in range(0,rowsPerBox*colsPerBox):
        for col in range(0,rowsPerBox*colsPerBox):
            if (row,col) in startState.keys():
                board[row][col] = startState[row,col][0]
    for row in range(0,rowsPerBox*colsPerBox):
        #fix [0:4] to work with all puzzles
            print(board[row][0:col+1])
else: print('no puzzle')

print('--------------------')

# Populate a list of choices for empty cells
totalChoices = rowsPerBox * colsPerBox
listOfChoices = []
for x in range(1, totalChoices + 1):
    listOfChoices.append(x)

print('Possible choices for empty cells: ', listOfChoices)

print('--------------------')

# Populate the empty cells with the list of choices
for row in range(0,rowsPerBox*colsPerBox):
    for col in range(0,rowsPerBox*colsPerBox):
        if board[col][row] == 0:
            board[col][row] = listOfChoices

# Board printing, can be deleted later
for row in board:
    print(row)

print('--------------------')

# >>>>> Solving logic <<<<<
rowCoordinates = []
colCoordinates = []
subGridTopLeftCoordinates = []
singleSubGrid = []

def generateRowCoordinates(rowNumber, rowsPerBox, colsPerBox):
    rowCoordinates.clear()
    for col in range(0,rowsPerBox*colsPerBox):
        if type(board[rowNumber][col]) == int:
            rowCoordinates.append([rowNumber, col])

def generateColumnCoordinates(colNumber, rowsPerBox, colsPerBox):
    colCoordinates.clear()
    for row in range(0,rowsPerBox*colsPerBox):
        if type(board[row][colNumber]) == int:
            colCoordinates.append([row, colNumber])

def generateTopLeftSubGridCoordinates(rowsPerBox, colsPerBox):
    if rowsPerBox == 1 or colsPerBox == 1:
        totalSubGrids = 1
    elif rowsPerBox == 0 or colsPerBox == 0:
        return
    else:
        totalSubGrids = (rowsPerBox*colsPerBox)
    subGridTopLeftCoordinates.clear()
    for i in range(0,totalSubGrids):
        x = (i//rowsPerBox)*rowsPerBox
        y = (i%rowsPerBox)*colsPerBox
        subGridTopLeftCoordinates.append([x, y])

def populateASubGrid(rowCord, colCord, rowsPerBox, colsPerBox):
    if rowsPerBox <= 1:
        rowsPerBox = colsPerBox
    if colsPerBox <= 1:
        colsPerBox = rowsPerBox
    for pair in subGridTopLeftCoordinates:
        singleSubGrid.append(pair)
        for x in range(1, rowsPerBox):
            singleSubGrid.append([(pair[0] + x), (pair[1])])
            for y in range(1, colsPerBox):
                singleSubGrid.append([(pair[0] + x), (pair[1]) + y])
        for y in range(1, colsPerBox):
                singleSubGrid.append([(pair[0]), (pair[1] + y)])
        if singleSubGrid.__contains__([rowCord, colCord]):
            return
        else:
            singleSubGrid.clear()

generateRowCoordinates(0, rowsPerBox, colsPerBox)
generateColumnCoordinates(0, rowsPerBox, colsPerBox)
generateTopLeftSubGridCoordinates(rowsPerBox, colsPerBox)
populateASubGrid(0, 0, rowsPerBox, colsPerBox)

print('row coords: ', rowCoordinates)
print('col clords: ', colCoordinates)
print('subgrid top left cords: ', subGridTopLeftCoordinates)
print('single subgrid: ', singleSubGrid)
#from asyncio.windows_events import NULL
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

row = 0
col = 0

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

# Populate the remaining cells with possible choices
totalChoices = rowsPerBox * colsPerBox
listOfChoices = []
for x in range(1, totalChoices + 1):
    listOfChoices.append(x)

print('Possible choices for empty cells: ', listOfChoices)

print('--------------------')

for row in range(0,rowsPerBox*colsPerBox):
    for col in range(0,rowsPerBox*colsPerBox):
        if board[col][row] == 0:
            board[col][row] = listOfChoices

for row in board:
    print(row)

print('--------------------')

# Solving logic

rowCoordinates = []
colCoordinates = []
subGridTopLeftCoordinates = []

def generateRowCoordinates(rowNumber):
    rowCoordinates.clear()
    for col in range(0,rowsPerBox*colsPerBox):
        if type(board[rowNumber][col]) == int:
            rowCoordinates.append([rowNumber, col])

def generateColumnCoordinates(colNumber):
    colCoordinates.clear()
    for row in range(0,rowsPerBox*colsPerBox):
        if type(board[row][colNumber]) == int:
            colCoordinates.append([row, colNumber])

def generateTopLeftSubGridCoordinates():
    totalSubGrids = (rowsPerBox*colsPerBox)
    subGridTopLeftCoordinates.clear()
    for i in range(0,totalSubGrids):
        x = (i//rowsPerBox)*rowsPerBox
        y = (i%colsPerBox)*colsPerBox
        subGridTopLeftCoordinates.append([x, y])

finalGrid = []
singleSubGrid = []
def populateAllSubGrids():
    finalGrid.clear()
    for pair in subGridTopLeftCoordinates:
        singleSubGrid.append(pair)
        for x in range(1, rowsPerBox):
            singleSubGrid.append([(pair[0] + x), (pair[1])])
            for y in range(1, colsPerBox):
                singleSubGrid.append([(pair[0] + x), (pair[1]) + y])
        for y in range(1, colsPerBox):
                singleSubGrid.append([(pair[0]), (pair[1] + y)])
        finalGrid.append(singleSubGrid)
        print(singleSubGrid)
        singleSubGrid.clear()

generateRowCoordinates(2)
generateColumnCoordinates(1)
generateTopLeftSubGridCoordinates()
populateAllSubGrids()

#print(rowCoordinates)
#print(colCoordinates)
print(subGridTopLeftCoordinates)
print(finalGrid)

for index in finalGrid:
    print(index)

# rows per box = 2
# cols per box = 2
# box 0: top-left (x,y):
# to find x (box#//rowsperbox)*rowsperbox, this is how you get (x,)
# to find y (box#%colsperbox)*colsperbox, this is how you get (,y)

# x-value: (0//2)*2 = 0 y-value: (0%2)*2 = 0, therefore you get (0,0)
# x-value: (1//2)*2 = 0 y-value: (1%2)*2 = 2, therefore you get (0,2)
# x-value: (2//2)*2 = 2 y-value: (2%2)*2 = 0, therefore you get (2,0)
# x-value: (3//2)*2 = 2 y-value: (3%2)*2 = 2, therefore you get (2,2)

# 0 0 - 0 0 
# 0 0 - 0 0 
# ---------
# 0 0 - 0 0 
# 0 0 - 0 0

# 0 0 0 - 0 0 0 - 0 0 0
# 0 0 0 - 0 0 0 - 0 0 0 
# 0 0 0 - 0 0 0 - 0 0 0 
# ----- - ----- - -----
# 0 0 0 - 0 0 0 - 0 0 0
# 0 0 0 - 0 0 0 - 0 0 0 
# 0 0 0 - 0 0 0 - 0 0 0 
# ----- - ----- - -----
# 0 0 0 - 0 0 0 - 0 0 0
# 0 0 0 - 0 0 0 - 0 0 0 
# 0 0 0 - 0 0 0 - 0 0 0 

'''if type(board[col][row]) != int: 
    count = 0
    list = []
    for listElem in board[col][row]:
        count += 1
    print('Total Number of elements : ', count)'''

#class SudokuBoard:
   # def __init__(startState,rowsPerBox, colPerBox):

#for row in range(0,rowsPerBox*colsPerBox):
    #for col in range(0,rowsPerBox*colsPerBox):
        #if type(board[row][col]) == int:
            #generateRowCoordinates(row)

#print('Name Of Puzzle=',name.firstChild.data)
#print('Rows per Box=',sRowsPerBox.firstChild.data)
#print('Cols per Box=',sColsPerBox.firstChild.data)
#print('If Well Formed=',wellFormed.firstChild.data)
#print('If Solvable=',solvable.firstChild.data)
#print('If uniquesoln =',uniqueSolution.firstChild.data)
#print('If PigeonHole decidable=',pigeonholeDecidable.firstChild.data)

#print(args.puzzle_name)
#print(args.solve_on_startup)
#print(args.time_delay)
#print(args.solution_name)
#print(args.exit_on_solve)

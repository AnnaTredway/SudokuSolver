from enum import unique
from xml.dom import minidom
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
import os
import argparse
from PuzzleSpecs import PuzzleSpecs
from Board import Board

if __name__ == '__main__':
    p = argparse.ArgumentParser(description='...')
    p.add_argument('--puzzle_name', required=False)
    p.add_argument('-solve_on_startup', default=False)
    p.add_argument('-time_delay', default=0)
    p.add_argument('-solution_name', default=0)
    p.add_argument('-exit_on_solve', default=False)
    args = p.parse_args()

file = args.puzzle_name
if os.path.isfile(file): 
   file = minidom.parse(file)

puzzle = PuzzleSpecs(file)
board = Board()
board.createBoard(puzzle.rowsPerBox, puzzle.colsPerBox, puzzle.startState, puzzle.solvable)
board.printBoard()
print("----------------------------")
board.populateBoard(puzzle.rowsPerBox, puzzle.colsPerBox)
board.printBoard()
print("----------------------------")

# >>>>> Solving logic <<<<<
rowCoordinates = []
colCoordinates = []
subGridTopLeftCoordinates = []
singleSubGrid = []

def generateRowCoordinates(rowNumber, rowsPerBox, colsPerBox):
    rowCoordinates.clear()
    for col in range(0,rowsPerBox*colsPerBox):
        if type(board.board[rowNumber][col]) == int:
            rowCoordinates.append([rowNumber, col])

def generateColumnCoordinates(colNumber, rowsPerBox, colsPerBox):
    colCoordinates.clear()
    for row in range(0,rowsPerBox*colsPerBox):
        if type(board.board[row][colNumber]) == int:
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

generateRowCoordinates(0, puzzle.rowsPerBox, puzzle.colsPerBox)
generateColumnCoordinates(0, puzzle.rowsPerBox, puzzle.colsPerBox)
generateTopLeftSubGridCoordinates(puzzle.rowsPerBox, puzzle.colsPerBox)
populateASubGrid(0, 0, puzzle.rowsPerBox, puzzle.colsPerBox)

print('row coords: ', rowCoordinates)
print('col clords: ', colCoordinates)
print('subgrid top left cords: ', subGridTopLeftCoordinates)
print('single subgrid: ', singleSubGrid)

# >>> File Selector <<<
# Hides root window for now
#Tk().withdraw() 
    # show an "Open" dialog box and return the path to the selected file
#file = askopenfilename()
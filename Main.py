from enum import unique
from xml.dom import minidom
import tkinter as tk  # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
import os
import argparse
from PuzzleSpecs import PuzzleSpecs
from Board import Board
from GUI import GUI
import copy

def main(args):
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

    #window = tk.Tk()
    #gui = GUI(window, puzzle)
    #gui.puzzleSpecs.config(text=puzzle.convertSpecsToText())
    #window.mainloop()

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

    #generateRowCoordinates(0, puzzle.rowsPerBox, puzzle.colsPerBox)
    #generateColumnCoordinates(0, puzzle.rowsPerBox, puzzle.colsPerBox)
    generateTopLeftSubGridCoordinates(puzzle.rowsPerBox, puzzle.colsPerBox)
    #populateASubGrid(0, 0, puzzle.rowsPerBox, puzzle.colsPerBox)

    def generateNumbersInSubGrid(subGrid):
        numbersInSubGrid = []
        for coordPair in subGrid:
            if type(board.board[coordPair[0]][coordPair[1]]) == int:
                numbersInSubGrid.append(board.board[coordPair[0]][coordPair[1]])
        return numbersInSubGrid
    
    def generateNumbersInRow(rowCoordinates):
        numbersInRow = []
        for coordPair in rowCoordinates:
            if type(board.board[coordPair[0]][coordPair[1]]):
                numbersInRow.append(board.board[coordPair[0]][coordPair[1]])
        return numbersInRow

    def generateNumbersInColumn(colCoordinates):
        numbersInCol = []
        for coordPair in colCoordinates:
            if type(board.board[coordPair[0]][coordPair[1]]):
                numbersInCol.append(board.board[coordPair[0]][coordPair[1]])
        return numbersInCol

    # Iterate through unsolved board
    stopSieve = False
    while stopSieve == False:
        for row in range(0,puzzle.rowsPerBox*puzzle.colsPerBox):
            for col in range(0,puzzle.rowsPerBox*puzzle.colsPerBox):
                singleSubGrid.clear()
                # If the current cell has a list of possible values
                if type(board.board[row][col]) != int:
                    # Generate its combinations of subgrid coordinate pairs
                    populateASubGrid(row, col, puzzle.rowsPerBox, puzzle.colsPerBox)
                    #print(singleSubGrid)

                    # Generate its combinations row coordinate pairs
                    generateRowCoordinates(row, puzzle.rowsPerBox, puzzle.colsPerBox)
                    #print(rowCoordinates)

                    # Generate its combinations column coordinate pairs
                    generateColumnCoordinates(col, puzzle.rowsPerBox, puzzle.colsPerBox)
                    #print(colCoordinates)

                    '''Go through the lists of generated coordinate pairs
                    And then respectively generate lists of numbers from the coordinate pairs
                    whose cell only contains one number'''

                    listOfSubGridNumbers = generateNumbersInSubGrid(singleSubGrid)
                    listOfRowNumbers = generateNumbersInRow(rowCoordinates)
                    listOfColNumbers = generateNumbersInColumn(colCoordinates)

                    # Start sieving against subgrid first
                    for number in board.board[row][col]:
                        if number in listOfSubGridNumbers:
                            temp = copy.copy(board.board[row][col])
                            temp.remove(number)
                            board.board[row][col] = temp
                            board.printBoard()
                            print("--------")
                    
                    # Sieve against row
                    for number in board.board[row][col]:
                        if number in listOfRowNumbers:
                            temp = copy.copy(board.board[row][col])
                            temp.remove(number)
                            board.board[row][col] = temp
                            board.printBoard()
                            print("--------")
                    
                    # Sieve against column
                    for number in board.board[row][col]:
                        if number in listOfColNumbers:
                            temp = copy.copy(board.board[row][col])
                            temp.remove(number)
                            board.board[row][col] = temp
                            board.printBoard()
                            print("--------")

                    # If the current cell has a list with only one number,
                    # remove the list and replace only the number
                    if len(board.board[row][col]) == 1:
                        temp = copy.copy(board.board[row][col])
                        board.board[row][col] = temp[0]
                        board.printBoard()
                        print("--------")

        # Check if any cells in the puzzle still contain more than one number
        counter = 0
        for row in range(0,puzzle.rowsPerBox*puzzle.colsPerBox):
            #for col in range(0,puzzle.rowsPerBox*puzzle.colsPerBox):
            if all(type(x) is int for x in board.board[row]) != True:
                counter = counter + 1

        if counter == 0:
            stopSieve = True
                            
        #input("Press enter to cont...")
    board.printBoard()


if __name__ == '__main__':
    p = argparse.ArgumentParser(description='...')
    p.add_argument('--puzzle_name', required=False)
    p.add_argument('-solve_on_startup', default=False)
    p.add_argument('-time_delay', default=0)
    p.add_argument('-solution_name', default=0)
    p.add_argument('-exit_on_solve', default=False)
    args = p.parse_args()

main(args)

# >>> File Selector <<<
# Hides root window for now
#Tk().withdraw() 
    # show an "Open" dialog box and return the path to the selected file
#file = askopenfilename()
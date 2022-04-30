from enum import unique
from tracemalloc import stop
from xml.dom import minidom
import tkinter as tk  # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename
import os
import argparse
from PuzzleSpecs import PuzzleSpecs
from Board import Board
from GUI import GUI
import copy
import time

def main(args):
    file = args.puzzle_name
    if os.path.isfile(file): 
        file = minidom.parse(file)

    puzzle = PuzzleSpecs(file)
    board = Board()
    board.createBoard(puzzle.rowsPerBox, puzzle.colsPerBox, puzzle.startState, puzzle.solvable, puzzle.wellFormed)
    #board.printBoard()
    #print("----------------------------")
    if board.board:
        board.populateBoard(puzzle.rowsPerBox, puzzle.colsPerBox)
        board.printBoard()
        stopSieve = False
    else:
        stopSieve = True
    #print("----------------------------")

    window = tk.Tk()
    gui = GUI(window, puzzle)
    gui.puzzleSpecs.config(text=puzzle.convertSpecsToText())
    gui.initialBoardCreation()
    window.update()
    time.sleep(3)
    
    def solve(flag):
        currentBoardState = []
        currentBoardState = copy.deepcopy(board.board)
        board.generateTopLeftSubGridCoordinates(puzzle.rowsPerBox, puzzle.colsPerBox)
        for row in range(0,puzzle.rowsPerBox*puzzle.colsPerBox):
            for col in range(0,puzzle.rowsPerBox*puzzle.colsPerBox):
                board.singleSubGrid.clear()
                # If the current cell has a list of possible values
                if type(board.board[row][col]) != int:
                    # Generate its combinations of subgrid coordinate pairs
                    board.populateASubGrid(row, col, puzzle.rowsPerBox, puzzle.colsPerBox)
                    #print(singleSubGrid)

                    # Generate its combinations row coordinate pairs
                    board.generateRowCoordinates(row, puzzle.rowsPerBox, puzzle.colsPerBox)
                    #print(rowCoordinates)

                    # Generate its combinations column coordinate pairs
                    board.generateColumnCoordinates(col, puzzle.rowsPerBox, puzzle.colsPerBox)
                    #print(colCoordinates)

                    '''Go through the lists of generated coordinate pairs
                    And then respectively generate lists of numbers from the coordinate pairs
                    whose cell only contains one number'''

                    listOfSubGridNumbers = board.generateNumbersInSubGrid(board.singleSubGrid)
                    listOfRowNumbers = board.generateNumbersInRow(board.rowCoordinates)
                    listOfColNumbers = board.generateNumbersInColumn(board.colCoordinates)

                    # Start sieving against subgrid first
                    for number in board.board[row][col]:
                        if number in listOfSubGridNumbers:
                            temp = copy.copy(board.board[row][col])
                            temp.remove(number)
                            board.board[row][col] = temp
                            #board.printBoard()
                            #print("--------")

                            gui.updateBoard(board.board)
                            window.update()
                            time.sleep(1)

                    
                    # Sieve against row
                    for number in board.board[row][col]:
                        if number in listOfRowNumbers:
                            temp = copy.copy(board.board[row][col])
                            temp.remove(number)
                            board.board[row][col] = temp
                            #board.printBoard()
                            #print("--------")

                            gui.updateBoard(board.board)
                            window.update()
                            time.sleep(1)
                    
                    # Sieve against column
                    for number in board.board[row][col]:
                        if number in listOfColNumbers:
                            temp = copy.copy(board.board[row][col])
                            temp.remove(number)
                            board.board[row][col] = temp
                            #board.printBoard()
                            #print("--------")

                            gui.updateBoard(board.board)
                            window.update()
                            time.sleep(1)

                    # If the current cell has a list with only one number,
                    # remove the list and replace only the number
                    if len(board.board[row][col]) == 1:
                        temp = copy.copy(board.board[row][col])
                        board.board[row][col] = temp[0]
                        #board.printBoard()
                        #print("--------")

                        gui.updateBoard(board.board)
                        window.update()
                        time.sleep(1)

        # Check if any cells in the puzzle still contain more than one number
        counter = 0
        for row in range(0,puzzle.rowsPerBox*puzzle.colsPerBox):
            #for col in range(0,puzzle.rowsPerBox*puzzle.colsPerBox):
            if all(type(x) is int for x in board.board[row]) != True:
                counter = counter + 1

        if counter == 0:
            stopSieve = True
            return stopSieve
        else:
            stopSieve = False

        if board.board == currentBoardState:
            stopSieve = True
            return stopSieve
        else:
            stopSieve = False

        board.printBoard()
        return stopSieve

    # Iterate through unsolved board
    while stopSieve == False:
        stopSieve = solve(stopSieve)

    window.mainloop()

# Parse command line arguments
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
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
from Solver import Solver

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
    solver = Solver(board, puzzle, window, gui)
    window.update()
    time.sleep(3)

    # Iterate through unsolved board
    while stopSieve == False:
        stopSieve = solver.solve()

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
import os
import tkinter as tk
from tkinter.filedialog import askopenfile
from xml.dom import minidom
from Board import Board
from PuzzleSpecs import PuzzleSpecs

# >>> File Selector <<<
# Hides root window for now
#tk.Tk().withdraw() 
    # show an "Open" dialog box and return the path to the selected file
#file = askopenfilename()

class GUI:
    # Functions
    def chooseFileClick(self):
        fileName = self.chooseFileEntry.get()

        if os.path.isfile(fileName):
            file = minidom.parse(fileName)
            self.puzzle = PuzzleSpecs(file)
            self.puzzleSpecs.config(text=self.puzzle.convertSpecsToText())
            self.initialBoardCreation()
        else:
            self.puzzleSpecs.config(text="Error. No such file or directory: " + self.chooseFileEntry.get())

    def fileSelector(self):
        fileName = askopenfile()
        file = minidom.parse(fileName)
        self.puzzle = PuzzleSpecs(file)
        self.puzzleSpecs.config(text=self.puzzle.convertSpecsToText())
        self.initialBoardCreation()

    def storePuzzleClick(self):
        storePuzzle = self.storePuzzleEntry.get()

    def __init__(self, window, puzzle, solveOnStartup):
        self.window = window
        self.puzzle = puzzle
        self.solveOnStartup = solveOnStartup

        # Declare widgets
        self.listOfFrames = []
        self.listOfLabels = []

        #specify puzzle as filename butoon
        self.chooseFileBtn = tk.Button(self.window, text="Specify puzzle as file name: ", command=self.chooseFileClick)
        self.chooseFileEntry = tk.Entry(self.window)
        #Enter step count
        self.stepCountLabel = tk.Label(self.window, text="Enter step count: ")
        self.stepCountEntry = tk.Entry(self.window)
        #step solver button
        self.stepTheSolverBtn = tk.Button(self.window, text="Complete the puzzle")
        # store Pluzzle button
        self.storePuzzleBtn = tk.Button(self.window, text="Store puzzle state as: ", command=self.storePuzzleClick)
        self.storePuzzleEntry = tk.Entry(self.window)
        self.puzzleSpecs = tk.Label(self.window, text="No active puzzle.")
        #file selector
        self.fileSelectBtn = tk.Button(self.window, text="Choose a file", command= self.fileSelector)

        # Add widgets to grid
        self.chooseFileBtn.grid(column=0, row=9)
        self.chooseFileEntry.grid(column=1, row=9)
        self.storePuzzleBtn.grid(column=2, row=9)
        self.storePuzzleEntry.grid(column=3, row=9)
        self.puzzleSpecs.grid(columnspan=4, row=10)
        self.stepTheSolverBtn.grid(column=0,row=11)
        self.stepCountLabel.grid(column=1,row=11)
        self.stepCountEntry.grid(column=2,row=11)
        self.fileSelectBtn.grid(column=3, row=11)

    def initialBoardCreation(self):
        rowwidth = 20
        rowheight = 4

        board = Board()
        board = board.createBoard(self.puzzle.rowsPerBox, self.puzzle.colsPerBox, self.puzzle.startState, self.puzzle.solvable, self.puzzle.wellFormed)

        for row in range(0,self.puzzle.rowsPerBox*self.puzzle.colsPerBox):
            for col in range(0,self.puzzle.rowsPerBox*self.puzzle.colsPerBox):
                frame = tk.Frame(master=self.window, highlightbackground='black', highlightthickness='2')
                frame.grid(row=row, column=col)
                label = tk.Label(frame, text=f'{board[row][col]}', height=rowheight, width=rowwidth, fg='black', bg='white')
                label.grid(row=row, column=col)
                self.listOfFrames.append(frame)
                self.listOfLabels.append(label)
            
    
    def updateBoard(self, board):
        rowwidth = 20
        rowheight = 4

        for frame in self.listOfFrames:
            temp = tk.Frame(frame)
            temp.destroy()
        for label in self.listOfLabels:
            temp = tk.Label(label)
            temp.destroy()
        
        self.listOfFrames.clear()
        self.listOfLabels.clear()

        for row in range(0,self.puzzle.rowsPerBox*self.puzzle.colsPerBox):
            for col in range(0,self.puzzle.rowsPerBox*self.puzzle.colsPerBox):
                frame = tk.Frame(master=self.window, highlightbackground='black', highlightthickness='2')
                frame.grid(row=row, column=col)
                label = tk.Label(frame, text=f'{board[row][col]}', height=rowheight, width=rowwidth, fg='black', bg='white')
                label.grid(row=row, column=col)
                self.listOfFrames.append(frame)
                self.listOfLabels.append(label)
import os
import tkinter as tk
from tkinter.filedialog import askopenfile
from xml.dom import minidom
from Board import Board
from PuzzleSpecs import PuzzleSpecs
# Right now, when you run the program, you can enter text into the text box.
# Thes press button, and it will display the text that was in the box elsewhere on the screen.

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
            puzzle = PuzzleSpecs(file)
            self.puzzle = PuzzleSpecs(file)
            self.puzzleSpecs.config(text=self.puzzle.convertSpecsToText())
        else:
            self.puzzleSpecs.config(text="Error. No such file or directory: " + self.chooseFileEntry.get())

    def storePuzzleClick(self):
        storePuzzle = self.storePuzzleEntry.get()
    
    #def grid(self):      
       

    def __init__(self, window, puzzle):
        self.window = window
        self.puzzle = puzzle

        # Declare widgets
        #specify puzzle as filename butoon
        self.chooseFileBtn = tk.Button(self.window, text="Specify puzzle as file name: ", command=self.chooseFileClick)
        self.chooseFileEntry = tk.Entry(self.window)
        #Enter step count
        self.stepCountLabel = tk.Label(self.window, text="Enter step count: ")
        self.stepCountEntry = tk.Entry(self.window)
        #step solver button
        self.stepTheSolverBtn = tk.Button(self.window, text="Step the Solver")
        # store Pluzzle button
        self.storePuzzleBtn = tk.Button(self.window, text="Store puzzle state as: ", command=self.storePuzzleClick)
        self.storePuzzleEntry = tk.Entry(self.window)

        self.puzzleSpecs = tk.Label(self.window, text="No active puzzle.")

        #grid tesing cases.
        # Add widgets to grid
        self.chooseFileBtn.grid(column=0, row=9)
        self.chooseFileEntry.grid(column=1, row=9)
        self.storePuzzleBtn.grid(column=2, row=9)
        self.storePuzzleEntry.grid(column=3, row=9)
        self.puzzleSpecs.grid(columnspan=4, row=10)
        self.stepTheSolverBtn.grid(column=0,row=11)
        self.stepCountLabel.grid(column=1,row=11)
        self.stepCountEntry.grid(column=2,row=11)
        

        
    def temp(self):
        self.puzzle
        #grid declaration
        dimOfGrid = self.puzzle.colsPerBox * self.puzzle.colsPerBox
        rowdim = coldim = dimOfGrid
        rowwidth = 20
        rowheight = 4

        labels = []
        #self.window.rowconfigure( [r for r in range(coldim)], weight=1, minsize=25)
        #self.window.columnconfigure( [c for c in range(coldim)], weight=1, minsize=25)
        
        Temp = Board()
        Temp = Temp.createBoard(self.puzzle.rowsPerBox, self.puzzle.colsPerBox, self.puzzle.startState, self.puzzle.solvable)

        for row in range(0,rowdim):
            for col in range(0,coldim):
                frame = tk.Frame(master = self.window, highlightbackground='black', highlightthickness='2' )
                frame.grid(row=row, column=col)
                label = tk.Label(frame, text=f'({Temp[row][col]})', height=rowheight, width=rowwidth, bg='white')
                label.grid(row=row, column=col)



'''for row in range(0,rowdim):
    for col in range(0,coldim):
        frame = tk.Frame(master = window, highlightbackground='black', highlightthickness='2' )
        frame.grid(row=row, column=col)
        for rowStart in range(0,self.puzzle.rowsPerBox*self.puzzle.colsPerBox):
            for colStart in range(0,self.puzzle.rowsPerBox*self.puzzle.colsPerBox):
                if (row,col) in self.puzzle.startState.keys():
                    labels[rowStart][colStart] = self.puzzle.startState[rowStart,colStart][0]
                    label = tk.Label(frame, text=f'({rowStart},{colStart})', height=rowheight, width=rowwidth, bg='white')
                    label.grid(row=row, column=col)'''
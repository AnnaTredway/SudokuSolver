import os
import tkinter as tk
from tkinter.filedialog import askopenfile
from xml.dom import minidom
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

    def __init__(self, window, puzzle):
        self.window = window
        self.puzzle = puzzle

        # Declare widgets
        self.chooseFileBtn = tk.Button(self.window, text="Specify puzzle as file name: ", command=self.chooseFileClick)
        self.chooseFileEntry = tk.Entry(self.window)

        self.storePuzzleBtn = tk.Button(self.window, text="Store puzzle state as: ", command=self.storePuzzleClick)
        self.storePuzzleEntry = tk.Entry(self.window)

        self.puzzleSpecs = tk.Label(self.window, text="No active puzzle.")

        # Add widgets to grid
        self.chooseFileBtn.grid(column=0, row=0)
        self.chooseFileEntry.grid(column=1, row=0)

        self.storePuzzleBtn.grid(column=2, row=0)
        self.storePuzzleEntry.grid(column=3, row=0)

        self.puzzleSpecs.grid(columnspan=4, row=1)
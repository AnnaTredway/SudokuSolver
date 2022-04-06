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

print(args.puzzle_name)
print(args.solve_on_startup)
print(args.time_delay)
print(args.solution_name)
print(args.exit_on_solve)

# Hides root window for now
# >>> File Selector <<<
#Tk().withdraw() 
    # show an "Open" dialog box and return the path to the selected file
#file = askopenfilename()

file='test_puzzle_specifications/3x3_06_solvable.xml'
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

print('Name Of Puzzle=',name.firstChild.data)
print('Rows per Box=',sRowsPerBox.firstChild.data)
print('Cols per Box=',sColsPerBox.firstChild.data)

print('If Well Formed=',wellFormed.firstChild.data)
print('If Solvable=',solvable.firstChild.data)
print('If uniquesoln =',uniqueSolution.firstChild.data)
print('If PigeonHole decidable=',pigeonholeDecidable.firstChild.data)
row = 0
col = 0
startState = eval(startState.firstChild.data.replace("\\","").replace("\n","").replace("\t",""))
rowsPerBox = int(sRowsPerBox.firstChild.data)
colsPerBox = int(sColsPerBox.firstChild.data)

# Creating the board
board = [
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
]



for row in range(0,rowsPerBox*rowsPerBox):
    for col in range(0,colsPerBox*colsPerBox):
        if (row,col) in startState.keys():
            board[row][col] = startState[row,col][0]

for row in range(0,rowsPerBox*rowsPerBox):
    print(board[row][0:10])




#class SudokuBoard:
   # def __init__(startState,rowsPerBox, colPerBox):







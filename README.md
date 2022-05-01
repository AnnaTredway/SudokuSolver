# SudokuSolver
Luke Poff and Anna Tredway

Main.py is the entry point to the project.

The backend logic is complete, however the GUI is lacking. Loading any puzzle via
command line will launch the gui and auto solve the puzzle. However, switching to another
puzzle without terminating the program has some kinks that needs to be worked out.

If better demonstration of the backend logic is needed, the print statements are left throughout the main.py, and solver.py code. The are currently commented out, but can be uncommented to see the complete functionality of the backend.

Main.py = entry point of the project (run this one)
Board.py = logic for creating and manipulating the board
Solver.py = contains the sieving logic
Gui.py = methods utilizing tkinter for GUI management
PuzzleSpecs.py = holds specs of current puzzle for easy access
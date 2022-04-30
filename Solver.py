import copy
import time

class Solver:
    def __init__(self, board, puzzle, window, gui):
        self.board = board
        self.puzzle = puzzle
        self.window = window
        self.gui = gui

    def solve(self):
        currentBoardState = []
        currentBoardState = copy.deepcopy(self.board.board)
        self.board.generateTopLeftSubGridCoordinates(self.puzzle.rowsPerBox, self.puzzle.colsPerBox)
        for row in range(0,self.puzzle.rowsPerBox*self.puzzle.colsPerBox):
            for col in range(0,self.puzzle.rowsPerBox*self.puzzle.colsPerBox):
                self.board.singleSubGrid.clear()
                # If the current cell has a list of possible values
                if type(self.board.board[row][col]) != int:
                    # Generate its combinations of subgrid coordinate pairs
                    self.board.populateASubGrid(row, col, self.puzzle.rowsPerBox, self.puzzle.colsPerBox)
                    #print(singleSubGrid)

                    # Generate its combinations row coordinate pairs
                    self.board.generateRowCoordinates(row, self.puzzle.rowsPerBox, self.puzzle.colsPerBox)
                    #print(rowCoordinates)

                    # Generate its combinations column coordinate pairs
                    self.board.generateColumnCoordinates(col, self.puzzle.rowsPerBox, self.puzzle.colsPerBox)
                    #print(colCoordinates)

                    '''Go through the lists of generated coordinate pairs
                    And then respectively generate lists of numbers from the coordinate pairs
                    whose cell only contains one number'''

                    listOfSubGridNumbers = self.board.generateNumbersInSubGrid(self.board.singleSubGrid)
                    listOfRowNumbers = self.board.generateNumbersInRow(self.board.rowCoordinates)
                    listOfColNumbers = self.board.generateNumbersInColumn(self.board.colCoordinates)

                    # Start sieving against subgrid first
                    for number in self.board.board[row][col]:
                        if number in listOfSubGridNumbers:
                            temp = copy.copy(self.board.board[row][col])
                            temp.remove(number)
                            self.board.board[row][col] = temp
                            #board.printBoard()
                            #print("--------")

                            self.gui.updateBoard(self.board.board)
                            self.window.update()
                            time.sleep(1)

                    
                    # Sieve against row
                    for number in self.board.board[row][col]:
                        if number in listOfRowNumbers:
                            temp = copy.copy(self.board.board[row][col])
                            temp.remove(number)
                            self.board.board[row][col] = temp
                            #board.printBoard()
                            #print("--------")

                            self.gui.updateBoard(self.board.board)
                            self.window.update()
                            time.sleep(1)
                    
                    # Sieve against column
                    for number in self.board.board[row][col]:
                        if number in listOfColNumbers:
                            temp = copy.copy(self.board.board[row][col])
                            temp.remove(number)
                            self.board.board[row][col] = temp
                            #board.printBoard()
                            #print("--------")

                            self.gui.updateBoard(self.board.board)
                            self.window.update()
                            time.sleep(1)

                    # If the current cell has a list with only one number,
                    # remove the list and replace only the number
                    if len(self.board.board[row][col]) == 1:
                        temp = copy.copy(self.board.board[row][col])
                        self.board.board[row][col] = temp[0]
                        #board.printBoard()
                        #print("--------")

                        self.gui.updateBoard(self.board.board)
                        self.window.update()
                        time.sleep(1)

        # Check if any cells in the puzzle still contain more than one number
        counter = 0
        for row in range(0,self.puzzle.rowsPerBox*self.puzzle.colsPerBox):
            #for col in range(0,puzzle.rowsPerBox*puzzle.colsPerBox):
            if all(type(x) is int for x in self.board.board[row]) != True:
                counter = counter + 1

        if counter == 0:
            stopSieve = True
            return stopSieve
        else:
            stopSieve = False

        if self.board.board == currentBoardState:
            stopSieve = True
            return stopSieve
        else:
            stopSieve = False

        self.board.printBoard()
        return stopSieve
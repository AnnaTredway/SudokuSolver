class Board:
    def __init__(self):
         self.board = []
         

    # Create initial m*n sized board based on puzzle specs
    def createBoard(self, rowsPerBox, colsPerBox, startState, solvable):
        #row = []
        gridline = []
        for col in range(0,colsPerBox*rowsPerBox):
            gridline.append(0)
        #grid = []
        for row in range(0,colsPerBox*rowsPerBox):
            self.board.append(list(gridline))

        # Populate board with inital starting state
        if rowsPerBox !=0 and colsPerBox !=0 and solvable == True and startState != 'none':
            for row in range(0,rowsPerBox*colsPerBox):
                for col in range(0,rowsPerBox*colsPerBox):
                    if (row,col) in startState.keys():
                        self.board[row][col] = startState[row,col][0]
        else: print('no puzzle')

        return self.board

    # Populate a the empty cells of the board with a list of possible choices
    def populateBoard(self, rowsPerBox, colsPerBox):
        # Create the intital list of possible choices
        totalChoices = rowsPerBox * colsPerBox
        listOfChoices = []
        for x in range(1, totalChoices + 1):
            listOfChoices.append(x)
        
        # Populate the empty cells with the list of choices
        for row in range(0,rowsPerBox*colsPerBox):
            for col in range(0,rowsPerBox*colsPerBox):
                if self.board[col][row] == 0:
                    self.board[col][row] = listOfChoices

    def printBoard(self):
        for row in self.board:
            print(row)
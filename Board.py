class Board:
    def __init__(self):
         self.board = []
         self.rowCoordinates = []
         self.colCoordinates = []
         self.subGridTopLeftCoordinates = []
         self.singleSubGrid = []

    # Create initial m*n sized board based on puzzle specs
    def createBoard(self, rowsPerBox, colsPerBox, startState, solvable, wellFormed):
        if wellFormed == True:
            #row = []
            gridline = []
            for col in range(0,colsPerBox*rowsPerBox):
                gridline.append(0)
            #grid = []
            for row in range(0,colsPerBox*rowsPerBox):
                self.board.append(list(gridline))

        # Populate board with inital starting state
        if rowsPerBox !=0 and colsPerBox !=0 and wellFormed == True and solvable == True and startState != 'none':
            for row in range(0,rowsPerBox*colsPerBox):
                for col in range(0,rowsPerBox*colsPerBox):
                    if (row,col) in startState.keys():
                        self.board[row][col] = startState[row,col][0]
        #else: print('no puzzle')

        return self.board

    # Populate a the empty cells of the board with a list of possible choices
    def populateBoard(self, rowsPerBox, colsPerBox):
        max = 0
        if rowsPerBox == 1 or colsPerBox == 1:
            if rowsPerBox > colsPerBox:
                max = rowsPerBox
            else:
                max = colsPerBox
            totalChoices = max * 2
        else:
            totalChoices = rowsPerBox * colsPerBox
        
        # Create the intital list of possible choices
        listOfChoices = []
        for x in range(1, totalChoices + 1):
            listOfChoices.append(x)
        
        # Populate the empty cells with the list of choices
        for row in range(0,rowsPerBox*colsPerBox):
            for col in range(0,rowsPerBox*colsPerBox):
                if self.board[col][row] == 0:
                    self.board[col][row] = listOfChoices

    # Print board by row
    def printBoard(self):
        for row in self.board:
            print(row)
    
    def generateRowCoordinates(self, rowNumber, rowsPerBox, colsPerBox):
        self.rowCoordinates.clear()
        for col in range(0,rowsPerBox*colsPerBox):
            if type(self.board[rowNumber][col]) == int:
                self.rowCoordinates.append([rowNumber, col])

    def generateColumnCoordinates(self, colNumber, rowsPerBox, colsPerBox):
        self.colCoordinates.clear()
        for row in range(0,rowsPerBox*colsPerBox):
            if type(self.board[row][colNumber]) == int:
                self.colCoordinates.append([row, colNumber])

    def generateTopLeftSubGridCoordinates(self, rowsPerBox, colsPerBox):
        if rowsPerBox == 1 or colsPerBox == 1:
            totalSubGrids = 1
        elif rowsPerBox == 0 or colsPerBox == 0:
            return
        else:
            totalSubGrids = (rowsPerBox*colsPerBox)
        self.subGridTopLeftCoordinates.clear()
        for i in range(0,totalSubGrids):
            x = (i//rowsPerBox)*rowsPerBox
            y = (i%rowsPerBox)*colsPerBox
            self.subGridTopLeftCoordinates.append([x, y])

    def populateASubGrid(self, rowCord, colCord, rowsPerBox, colsPerBox):
        if rowsPerBox <= 1:
            rowsPerBox = colsPerBox
        if colsPerBox <= 1:
            colsPerBox = rowsPerBox
        for pair in self.subGridTopLeftCoordinates:
            self.singleSubGrid.append(pair)
            for x in range(1, rowsPerBox):
                self.singleSubGrid.append([(pair[0] + x), (pair[1])])
                for y in range(1, colsPerBox):
                    self.singleSubGrid.append([(pair[0] + x), (pair[1]) + y])
            for y in range(1, colsPerBox):
                    self.singleSubGrid.append([(pair[0]), (pair[1] + y)])
            if self.singleSubGrid.__contains__([rowCord, colCord]):
                return
            else:
                self.singleSubGrid.clear()

    def generateNumbersInSubGrid(self, subGrid):
        numbersInSubGrid = []
        for coordPair in subGrid:
            if type(self.board[coordPair[0]][coordPair[1]]) == int:
                numbersInSubGrid.append(self.board[coordPair[0]][coordPair[1]])
        return numbersInSubGrid
    
    def generateNumbersInRow(self, rowCoordinates):
        numbersInRow = []
        for coordPair in rowCoordinates:
            if type(self.board[coordPair[0]][coordPair[1]]):
                numbersInRow.append(self.board[coordPair[0]][coordPair[1]])
        return numbersInRow

    def generateNumbersInColumn(self, colCoordinates):
        numbersInCol = []
        for coordPair in colCoordinates:
            if type(self.board[coordPair[0]][coordPair[1]]):
                numbersInCol.append(self.board[coordPair[0]][coordPair[1]])
        return numbersInCol
    
    def generateRowCoordinates(self, rowNumber, rowsPerBox, colsPerBox):
        self.rowCoordinates.clear()
        for col in range(0,rowsPerBox*colsPerBox):
            if type(self.board[rowNumber][col]) == int:
                self.rowCoordinates.append([rowNumber, col])

    def generateColumnCoordinates(self, colNumber, rowsPerBox, colsPerBox):
        self.colCoordinates.clear()
        for row in range(0,rowsPerBox*colsPerBox):
            if type(self.board[row][colNumber]) == int:
                self.colCoordinates.append([row, colNumber])

    def generateTopLeftSubGridCoordinates(self, rowsPerBox, colsPerBox):
        if rowsPerBox == 1 or colsPerBox == 1:
            totalSubGrids = 1
        elif rowsPerBox == 0 or colsPerBox == 0:
            return
        else:
            totalSubGrids = (rowsPerBox*colsPerBox)
        self.subGridTopLeftCoordinates.clear()
        for i in range(0,totalSubGrids):
            x = (i//rowsPerBox)*rowsPerBox
            y = (i%rowsPerBox)*colsPerBox
            self.subGridTopLeftCoordinates.append([x, y])

    def populateASubGrid(self, rowCord, colCord, rowsPerBox, colsPerBox):
        if rowsPerBox <= 1:
            rowsPerBox = colsPerBox
        if colsPerBox <= 1:
            colsPerBox = rowsPerBox
        for pair in self.subGridTopLeftCoordinates:
            self.singleSubGrid.append(pair)
            for x in range(1, rowsPerBox):
                self.singleSubGrid.append([(pair[0] + x), (pair[1])])
                for y in range(1, colsPerBox):
                    self.singleSubGrid.append([(pair[0] + x), (pair[1]) + y])
            for y in range(1, colsPerBox):
                    self.singleSubGrid.append([(pair[0]), (pair[1] + y)])
            if self.singleSubGrid.__contains__([rowCord, colCord]):
                return
            else:
                self.singleSubGrid.clear()
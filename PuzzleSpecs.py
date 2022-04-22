import os
from xml.dom import minidom

class PuzzleSpecs:

    def __init__(self, file):
        self.file = file
        self.name = self.file.getElementsByTagName('name')[0].firstChild.data
        self.rowsPerBox = int(self.file.getElementsByTagName('rows_per_box')[0].firstChild.data)
        self.colsPerBox = int(self.file.getElementsByTagName('cols_per_box')[0].firstChild.data)
        
        startState = self.file.getElementsByTagName('start_state')[0]
        try:    
            self.startState = eval(startState.firstChild.data.replace("\\","").replace("\n","").replace("\t",""))
        except: self.startState = 'none'

        self.wellFormed = bool(self.file.getElementsByTagName('well_formed')[0].firstChild.data)
        self.solvable = bool(self.file.getElementsByTagName('solvable')[0].firstChild.data)
        self.uniqueSolution = bool(self.file.getElementsByTagName('unique_solution')[0].firstChild.data)
        self.pigeonholeDecidable = bool(self.file.getElementsByTagName('pigeonhole_decidable')[0].firstChild.data)
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

        self.wellFormed = eval(self.file.getElementsByTagName('well_formed')[0].firstChild.data)
        self.solvable = eval(self.file.getElementsByTagName('solvable')[0].firstChild.data)
        self.uniqueSolution = eval(self.file.getElementsByTagName('unique_solution')[0].firstChild.data)
        self.pigeonholeDecidable = eval(self.file.getElementsByTagName('pigeonhole_decidable')[0].firstChild.data)
    
    def convertSpecsToText(self):
        text = self.name + ": "
        if self.wellFormed == True:
            text += "is well-formed, "
        else:
            text += "is not well-formed, "
        if self.solvable == True:
            text += "is solvable, "
        else:
            text+= "is not solvable, "
        if self.uniqueSolution == True:
            text += "has unique solution, "
        else:
            text += "does not have unique solution, "
        if self.pigeonholeDecidable == True:
            text += "is pigeonhole-decidable"
        else:
            text += "is not pigeonhole-decidable"
        
        return text
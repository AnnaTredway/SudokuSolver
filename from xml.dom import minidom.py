from enum import unique
from xml.dom import minidom

# parse an xml file by name
file = minidom.parse('0x0_03_solvable.xml')

# Retrieve puzzle elements
name = file.getElementsByTagName('name')[0]
rowsPerBox = file.getElementsByTagName('rows_per_box')[0]
colsPerBox = file.getElementsByTagName('cols_per_box')[0]
startState = file.getElementsByTagName('start_state')[0]
wellFormed = file.getElementsByTagName('well_formed')[0]
solvable = file.getElementsByTagName('solvable')[0]
uniqueSolution = file.getElementsByTagName('unique_solution')[0]
pigeonholeDecidable = file.getElementsByTagName('pigeonhole_decidable')[0]

# The below print statements are temporary. They are used to ensure the values from the xml doc are pulled correctly.
# The above hardcoded xml provides no data for the starting state of a puzzle, so the startState variable is null in this case.
# You cannot print a null value, so the startSate print statement is commented out to prevent errors.

print(name.firstChild.data)
print(rowsPerBox.firstChild.data)
print(colsPerBox.firstChild.data)
#print(startState.firstChild.data)
print(wellFormed.firstChild.data)
print(solvable.firstChild.data)
print(uniqueSolution.firstChild.data)
print(pigeonholeDecidable.firstChild.data)
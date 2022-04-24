import tkinter as tk

window = tk.Tk()

# Right now, when you run the program, you can enter text into the text box.
# Thes press button, and it will display the text that was in the box elsewhere on the screen.

# Functions
def chooseFileClick():
    fileName = fileEntry.get()
    myLabel = tk.Label(window, text=fileName)
    myLabel.grid(column=0, row=1)

# Declare widgets
chooseFileBtn = tk.Button(window, text="Specify puzzle as file name: ", command=chooseFileClick)
fileEntry = tk.Entry(window)

# Add widgets to grid
chooseFileBtn.grid(column=0, row=0)
fileEntry.grid(column=1, row=0)

window.mainloop()
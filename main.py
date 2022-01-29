# Web Text Reader

# This program will display all the text content of a given url, in plain text format
# The purpose of this was largely to be able to view NZ Herald premium articles, but it works on any site


import tkinter as tk
from FrameMain import *
from functions import *


class Window:
    def __init__(self, root, title, geometry):
        # This will set all the base info for the main window
        self.root = root
        self.root.title(title)
        self.root.geometry(geometry)

        # To allow the expandability of all the rows and columns needed
        root.columnconfigure([0], weight=1)
        root.rowconfigure([1], weight=1)

        FrameMain(root)  # To make the main frame

        self.root.mainloop()  # To actually run the program loop


def main():
    window = Window(tk.Tk(), 'Web Text Reader', '1200x1000')  # Main window defined here


main()

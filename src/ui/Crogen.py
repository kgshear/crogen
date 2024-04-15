from tkinter import Tk
class Crogen(Tk):
    def __init__(self):
        super().__init__()
        self.title('Crogen')
        start_width = 1395
        start_height = 800
        self.geometry(f"{start_width}x{start_height}")

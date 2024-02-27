# contains the whole tkinter application

import tkinter as tk
class Crogen(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Crogen')





if __name__ == '__main__':
    app = Crogen()
    app.mainloop()

from src.ui.Detail.build import DetailView
from src.ui.Creation.build import CreationView
from src.ui.Pattern.build import PatternView
from src import Crogen

class View:
    def __init__(self):
        self.root = None  # Initialize root as None
        self.frame_classes = {
            "detail": DetailView,
            "creation": CreationView,
            "pattern": PatternView,
        }
        self.current_frame = None

    def initialize_root(self):
        if self.root is None:  # Only create root if it's not already created
            self.root = Crogen.Crogen()

    def switch(self, name):
        new_frame = self.frame_classes[name](self.root)
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame = new_frame
        self.current_frame.grid(row=0, column=0, sticky="nsew")


    def start_mainloop(self):
        self.root.mainloop()


if __name__ == '__main__':
    view = View()
    view.initialize_root()  # Initialize the root window
    view.start_mainloop()

from src.ui.Detail.build.DetailView import DetailView
from src.ui.Creation.build.CreationView import CreationView
from src.ui.Pattern.build.PatternView import PatternView
from src.ui import Crogen


class View:
    def __init__(self):
        self.root = Crogen.Crogen()  # Initialize root as None
        self.frame_classes = {}
        self._add_frame(PatternView, "pattern")
        self._add_frame(CreationView, "creation")
        self._add_frame(DetailView, "detail")





    def _add_frame(self, Frame, name):
        self.frame_classes[name] = Frame(self.root)
        self.frame_classes[name].grid(row=0, column=0, sticky="nsew")

    def switch(self, name):
        #if self.current_frame is not None:
        #    self.current_frame.destroy()
        self.frame_classes[name].tkraise()
        #self.current_frame.grid(row=0, column=0, sticky="nsew")



    def start_mainloop(self):
        self.root.mainloop()


if __name__ == '__main__':
    view = View()
    view.start_mainloop()
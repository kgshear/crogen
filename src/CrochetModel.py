import CrochetStitch
import PatternObserver

class CrochetModel:
    # use method to add

    def __init__(self):
        self.row_length = 0
        self.observers = []
        self.cur_row = CrochetStitch.Row()
        self.rows = []

    def addRow(self):
        pass

    def addStitch(self, type: CrochetStitch):
        self.cur_row.add_stitch(type)
        self.notifyObservers()

    def build(self):
        # check to see if there are any stitches or rows
        # return Pattern Object
        pass

    def redo(self):
        pass

    def undo(self):
        pass

    def addObserver(self, observer: PatternObserver):
        self.observers.append(observer)

    def removeObserver(self, observer: PatternObserver):
        self.observers.remove(observer)

    def notifyObservers(self):
        for observer in self.observers:
            observer.update(self)

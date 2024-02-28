import CrochetStitch
import PatternObserver

class CrochetModel:
    # use method to add
    row_length: int = 0

    def __init__(self):
       self.observers = []

    def addRow(self):
        pass

    def addStitch(self, type: CrochetStitch):
        pass

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

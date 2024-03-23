from .DetailController import DetailController
from .CreationController import CreationController
from .PatternController import PatternController
from src.models.CrochetModel import CrochetModel
from src.ui.View import View

class Controller:
    def __init__(self, model: CrochetModel, view: View):
        self.view = view
        self.model = model


        self.pattern_controller = PatternController(model, view)
        self.creation_controller = CreationController(model, view)
        self.detail_controller = DetailController(model, view)

    def start(self):
        self.view.start_mainloop()
        # self.view.switch("detail")


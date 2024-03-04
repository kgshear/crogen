import DetailController
import CreationController
import PatternController
from src.CrochetModel import CrochetModel
from src.ui.View import View

class Controller:
    def __init__(self, model: CrochetModel, view: View):
        self.view = view
        self.model = model
        self.detail_controller = DetailController(model, view)
        self.creation_controller = CreationController(model, view)
        self.pattern_controller = PatternController(model, view)


from src.CrochetModel import CrochetModel
from src.ui.View import View

class DetailController:
    def __init__(self, model: CrochetModel, view: View):
        self.view = view
        self.model = model

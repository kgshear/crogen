from src.models.CrochetModel import CrochetModel
from src.ui.View import View

class PatternController:
    def __init__(self, model: CrochetModel, view: View):
        self.view = view
        self.model = model
        self.frame = self.view.frame_classes["pattern"]
        self._bind()


    def _bind(self):
        self.frame.BackButton.config(command=self.back_command)

    def back_command(self):
        self.view.switch("creation")
        print("Switching from pattern to creation")
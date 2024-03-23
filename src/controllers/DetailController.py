from src.models.CrochetModel import CrochetModel
from src.ui.View import View

class DetailController:
    def __init__(self, model: CrochetModel, view: View):
        self.view = view
        self.model = model
        self.frame = self.view.frame_classes["detail"]
        self._bind()
        print(self.frame)


    def _bind(self):
        self.frame.NextButton.config(command=self.next_command)

    def next_command(self):
        self.view.switch("creation")
        print("switching from detail to creation")

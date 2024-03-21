from src.models.CrochetModel import CrochetModel
from src.ui.View import View

class CreationController:
    def __init__(self, model: CrochetModel, view: View):
        self.view = view
        self.model = model
        self.frame = self.view.frame_classes["creation"]
        self._bind()

    def _bind(self):
        self.frame.ClearButton.config(command=self.clear_command())
        self.frame.AddButton.config(command=self.add_command())
        self.frame.RepeatButton.config(command=self.repeat_command())
        self.frame.UndoButton.config(command=self.undo_command())
        self.frame.CreateButton.config(command=self.create_command())
        self.frame.BackButton.config(command=self.back_command())


    def add_command(self):
        pass

    def repeat_command(self):
        pass

    def undo_command(self):
        pass

    def clear_command(self):
        pass

    def create_command(self):
        pass

    def back_command(self):
        pass



from src.models.CrochetModel import CrochetModel
from src.ui.View import View

class PatternController:
    def __init__(self, model: CrochetModel, view: View):
        self.view = view
        self.model = model
        self.frame = self.view.frame_classes["pattern"]
        written_pattern = self.model.generate_written_pattern()

        self._bind()


    def _bind(self):
        self.frame.BackButton.config(command=self.back_command)
        self.frame.CopyButton.config(command=self.copy_command)

    def back_command(self):
        self.view.switch("creation")

    def copy_command(self):
        content = self.frame.canvas.itemcget(self.frame.pattern_text, "text")
        self.view.root.clipboard_clear()
        self.view.root.clipboard_append(content)
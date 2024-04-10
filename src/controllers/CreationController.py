from src.models.CrochetModel import CrochetModel
from src.ui.View import View
import os
from tkinter import PhotoImage

class CreationController:
    def __init__(self, model: CrochetModel, view: View):
        self.view = view
        self.model = model
        self.frame = self.view.frame_classes["creation"]
        self._bind()

    def _bind(self):
        self.frame.ClearButton.config(command=self.clear_command)
        self.frame.AddButton.config(command=self.add_command)
        self.frame.NewButton.config(command=self.new_command)
        self.frame.UndoButton.config(command=self.undo_command)
        self.frame.RedoButton.config(command=self.redo_command)
        self.frame.CreateButton.config(command=self.create_command)
        self.frame.BackButton.config(command=self.back_command)

    def add_command(self):
        isRedo = False
        amount = self.frame.amount_select.get()
        stitch_type = self.frame.stitch_type.get()
        if amount.isnumeric():
            amount = int(amount)
            if amount > 100:
                pass
            else:
                self.model.addToRow(stitch_type, amount, isRedo)
                self.update_image()
        else:
            pass
        self.frame.update_row_count(self.model.get_row_count())
        self.frame.update_stitch_count(self.model.get_stitch_count())
        self.frame.canvas.update_idletasks()

    def new_command(self):
        isRedo = False
        self.model.newRow(isRedo)

    def undo_command(self):
        self.model.undo()
        self.frame.update_row_count(self.model.get_row_count())
        self.frame.update_stitch_count(self.model.get_stitch_count())
        self.update_image()
        self.frame.canvas.update_idletasks()


    def redo_command(self):
        self.model.redo()
        self.frame.update_row_count(self.model.get_row_count())
        self.frame.update_stitch_count(self.model.get_stitch_count())
        self.update_image()
        self.frame.canvas.update_idletasks()

    def clear_command(self):
        self.model.clearPattern()
        self.frame.update_row_count(self.model.get_row_count())
        self.frame.update_stitch_count(self.model.get_stitch_count())
        self.frame.set_empty()
        self.frame.canvas.update_idletasks()


    def create_command(self):
        self.view.switch("pattern")
        written_pattern = self.model.generate_written_pattern()
        next_frame = self.view.frame_classes["pattern"]
        next_frame.update_pattern(written_pattern)
        next_frame.canvas.update_idletasks()

        print("switching from creation to pattern")

    def back_command(self):
        self.view.switch("detail")
        print("switching from creation to detail")

    def update_image(self):
        self.frame.update_png()
        self.frame.canvas.itemconfig(self.frame.model_object, image=self.frame.model_image)
        self.frame.canvas.update_idletasks()
        print("called update")





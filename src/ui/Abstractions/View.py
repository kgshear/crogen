import tkinter as tk
from tkinter import ttk

class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.controller = None

    def set_controller(self, controller):
        self.controller = controller


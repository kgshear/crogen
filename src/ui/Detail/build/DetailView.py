
from pathlib import Path

from tkinter import Canvas, Button, PhotoImage, Tk, Frame

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class DetailView(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(bg= "#FFFFFF")


        self.canvas = Canvas(
            self,
            bg = "#FFFFFF",
            height = 800,
            width = 1395,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
    
        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            0.0,
            326.0,
            1440.0,
            925.0,
            fill="#BBA1DC",
            outline="")
    
        self.canvas.create_text(
            180.0,
            385.0,
            anchor="nw",
            text="Design your own Pattern!",
            fill="#FFFFFF",
            font=("Karla Bold", 48 * -1)
        )
    
        self.canvas.create_text(
            238.0,
            636.0,
            anchor="nw",
            text="Yarn Size:",
            fill="#FFFDFD",
            font=("Karla Bold", 40 * -1)
        )
    
        self.canvas.create_text(
            238.0,
            498.0,
            anchor="nw",
            text="Pattern Type:",
            fill="#FFFFFF",
            font=("Karla Bold", 40 * -1)
        )
    
        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))


    
        self.canvas.create_rectangle(
            542.0,
            498.0,
            903.0,
            545.0,
            fill="#FFFFFF",
            outline="")
    
        self.canvas.create_text(
            640.0,
            503.0,
            anchor="nw",
            text="select type",
            fill="#000000",
            font=("Karla Regular", 32 * -1)
        )
    
        self.canvas.create_rectangle(
            542.0,
            636.0,
            903.0,
            683.0,
            fill="#FFFFFF",
            outline="")
    
        self.canvas.create_text(
            644.0,
            642.0,
            anchor="nw",
            text="select size",
            fill="#000000",
            font=("Karla Regular", 32 * -1)
        )
    
        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            677.0,
            152.0,
            image=self.image_image_1
        )
    
        self.canvas.create_rectangle(
            177.0,
            453.0,
            1028.0,
            459.0,
            fill="#FFFFFF",
            outline="")
        # parent.resizable(False, False)
        # parent.mainloop()
        self.canvas.pack()
        self.NextButton = Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.NextButton.place(
            x=1070.0,
            y=679.0,
            width=296.0,
            height=94.0
        )
    



from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# def PatternView(parent):
class PatternView(Frame):
    def __init__(self, *args, **kwargs):
        self.written_pattern = ""
        super().__init__(*args, **kwargs)

        self.configure(bg = "#FFFFFF")


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
            163.0,
            1440.0,
            906.0,
            fill="#BBA1DC",
            outline="")

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.BackButton = Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.BackButton.place(
            x=43.0,
            y=694.0,
            width=296.0,
            height=94.0
        )
        # self.BackButton.pack()

        self.canvas.create_text(
            77.0,
            181.0,
            anchor="nw",
            text="Written Pattern:",
            fill="#FFFFFF",
            font=("Karla Bold", 48 * -1)
        )

        self.pattern_text = self.canvas.create_text(
            113.0,
            249.0,
            anchor="nw",
            text="",
            fill="#FFFFFF",
            font=("Karla Regular", 24 * -1)
        )

        self.canvas.create_rectangle(
            1398.0,
            553.0,
            1418.0,
            671.0,
            fill="#D9D9D9",
            outline="")

        self.canvas.create_rectangle(
            1398.0,
            522.0,
            1418.0,
            545.0,
            fill="#000000",
            outline="")

        self.canvas.create_rectangle(
            1398.0,
            818.0,
            1418.0,
            841.0,
            fill="#000000",
            outline="")

        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            147.0,
            76.0,
            image=self.image_image_1
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.CopyButton = Button(
            self,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.CopyButton.place(
            x=1167,
            y=181,
            width=184.0,
            height=77.48383331298828
        )

        self.canvas.create_rectangle(
            74.0,
            234.0,
            925.0,
            240.0,
            fill="#FFFFFF",
            outline="")
        # parent.resizable(False, False)
        # parent.mainloop()
        self.canvas.pack()

    def update_pattern(self, written_pattern):
        self.canvas.itemconfigure(self.pattern_text, text=written_pattern)

